from configparser import ConfigParser
import os

class Config:
    def __init__(self, config_file="uiconfigfile.ini"):
        self.config = ConfigParser()
        # Get the directory where this file is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, config_file)
        self.config.read(config_path)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS", "").split(", ")

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS", "").split(", ")

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS", "").split(", ")

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE", "LangGraph Agentic AI")

    
