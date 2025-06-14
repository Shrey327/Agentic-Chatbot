from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition,ToolNode
from src.langgraphagenticai.nodes.chatbot_with_Tool_node import ChatbotWithToolNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph with a single node that takes user input and returns a response.
        """
        chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot") 
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds a chatbot with tools graph with a single node that takes user input and returns a response.
        """
        #Define the tools and the tool nodes
        tools = get_tools()
        tool_node = create_tool_node(tools)

        ### define the llm
        llm = self.llm

        ##define the chatbot node
        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)
        ##add nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        #define conditional edges and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        

    def setup_graph(self, usecase):
        """
        Setup the graph based on the use case
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()
        else:
            raise ValueError(f"Invalid use case: {usecase}")
        
        # Compile the graph before returning
        return self.graph_builder.compile()