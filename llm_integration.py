# src/llm_integration.py
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

class AzureLLM:
    """
    A wrapper class for interacting with Azure OpenAI Chat models.
    """
    def __init__(self):
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        """
        Initializes the AzureChatOpenAI model using environment variables.
        """
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION")

        if not all([api_key, endpoint, deployment_name, api_version]):
            raise ValueError("Missing one or more Azure OpenAI environment variables.")

        print(f"Initializing AzureChatOpenAI with deployment: {deployment_name}")
        return AzureChatOpenAI(
            deployment_name=deployment_name,
            model=deployment_name, # Use deployment name as model as per your config
            temperature=0,
            api_version=api_version,
            api_key=api_key,
            azure_endpoint=endpoint
        )

    def generate_response(self, system_message_content: str, user_message_content: str) -> str:
        """
        Sends a query to the LLM and returns its response.

        Args:
            system_message_content (str): The system prompt to guide the LLM.
            user_message_content (str): The user's input/query.

        Returns:
            str: The content of the LLM's response.
        """
        messages = [
            SystemMessage(content=system_message_content),
            HumanMessage(content=user_message_content),
        ]
        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            print(f"Error generating LLM response: {e}")
            return f"An error occurred: {e}"

# Example usage (for testing)
if __name__ == "__main__":
    try:
        azure_llm = AzureLLM()
        response_content = azure_llm.generate_response(
            system_message_content="You are a helpful assistant.",
            user_message_content="What is the capital of France?"
        )
        print("LLM Test Response:", response_content)
    except ValueError as e:
        print(f"Configuration error: {e}. Please check your .env file.")
    except Exception as e:
        print(f"An unexpected error occurred during LLM test: {e}")