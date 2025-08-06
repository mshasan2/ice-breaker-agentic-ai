import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrapes a LinkedIn profile page.

    Args:
        linkedin_profile_url (str): The URL of the LinkedIn profile to scrape.
        mock (bool): If True, returns a mock response instead of scraping.

    Returns:
        str: The text content of the LinkedIn profile.
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/mshasan2/c668ea1b82c6829e1ab985e1b16bc246/raw/329fa56326cceb152f2fc607e84d4d5f6cbda239/mohammedsadath-hasan-scrapin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/v1/enrichment/profile"
        params = {
            "apikey": os.getenv("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)
    data = response.json().get("person")
    if not data:
        return {}

    data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["certifications"]
        }

    return data



if __name__ == "__main__":
    print(scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/hasan-mohammedsadath/", mock=True))