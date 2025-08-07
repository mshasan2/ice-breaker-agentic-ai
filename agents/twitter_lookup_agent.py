import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub
from tools.tools import get_profile_url_tavily

load_dotenv()

def lookup(name:str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_retries=2
    )

    # Template containing the output indicator
    template = """Given the name {name_of_person} I want you to get me a link to their Twitter/X profile page
                    and extract from it their username.
                    Your final response should contain only person's username
                    If you can't find one, output only 'None'"""
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    # Define the tool to be used by the agent
    tools_for_agent = [
        Tool(
            name="Crawl Tavily for Twitter/X Profile Page",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the Twitter/X Username",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    # AgentExecutor is used to run the agent in an environment where it can call tools
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )

    twitter_username = result["output"]
    return twitter_username

if __name__ == "__main__":
    twitter_username = lookup(name="Elon Musk")
    print(twitter_username)