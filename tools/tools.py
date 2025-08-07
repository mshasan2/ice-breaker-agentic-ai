# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch

def get_profile_url_tavily(name:str):
    """Searches for LinkedIn or Twitter Profile Page"""
    #search = TavilySearchResults() - Depricated
    search = TavilySearch()
    res = search.run(f"{name}")
    return res
