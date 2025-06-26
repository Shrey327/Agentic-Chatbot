from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
from langchain_community.tools import ArxivQueryRun
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.utilities import ArxivAPIWrapper
def get_tools():
    """
    Get the tools for the chatbot with web
    """
    api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=2,doc_content_chars_max=500)
    arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv)
    api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=2,doc_content_chars_max=500)
    wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki)
    tavily = TavilySearchResults(max_results=2)
    tools = [arxiv,wiki,tavily]
    return tools


def create_tool_node(tools):
    """
    create the tool node for the chatbot 
    """
    return ToolNode(tools=tools)
