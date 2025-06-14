from src.langgraphagenticai.state.state import State

class ChatbotWithToolNode:
    """
    chatbot with tool node
    """
    def __init__(self,model):
        self.llm = model
    
    def process(self, state: State)->dict:
        """
        Process the user input and return the response
        """

        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role":"user","content":user_input}])

        tools_response = f"Tools integration for : '{user_input}'"

        return {"messages": [llm_response,tools_response]}


    def create_chatbot(self,tools):
        """
        Return the chatbot with tool node
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the user input and return the response
            """

            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node

