from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os
from third_parties.linkedin import scrape_linkedin_profile
from agents.linked_lookup_agent import lookup as linked_lookup_agent
from third_parties.twitter import scrape_user_tweets
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from output_parsers import summary_parser, Summary
from typing import Tuple


def ice_break_with(name: str, mock: bool = False) -> Tuple[Summary, str]:
    linkedin_profile_url = linked_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url, mock=mock)

    twitter_username = twitter_lookup_agent(name=name)
    user_tweets = scrape_user_tweets(username=twitter_username, mock=mock)

    # Defining the template and language/chat model
    summary_template = """
            Given the information about a person from Linkedin {information} 
            and their latest Twitter posts/tweets {twitter_posts},  I want you to create:
            1. a short summary
            2. two interesting facts about them
            
            Use both information from Linkedin and Twitter to create the summary and facts.
            \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variable=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3")
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )

    # Creating a chain
    # Store the API Key as an environment variable
    chain = summary_prompt_template | llm | summary_parser
    res: Summary = chain.invoke(input={"information": linkedin_data, "twitter_posts": user_tweets})

    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    load_dotenv()
    print("Start")
    ice_break_with(name="Harrison Chase")
