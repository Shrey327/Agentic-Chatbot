import streamlit as st
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_app():
    """
    Load the LangGraph Agentic AI application with Streamlit UI.
    """
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    # Here you can add more logic to handle the user controls
    if not user_input:
        st.error("No user input received. Please select options from the sidebar.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            ##configuring the llm
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize the model. Please check the API key and model name.")
                return

            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Please select a use case from the sidebar.")
                return

            ##building the graph
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error building the graph: {e}")
                return

            
            

        except Exception as e:
            st.error(f"Error in the application: {e}")
            return

