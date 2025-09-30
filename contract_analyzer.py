# src/contract_analyzer.py
from src.llm_integration import AzureLLM
from src.contract_parser import ContractParser
from src.prompt_templates import CHATBOT_SYSTEM_PROMPT
import json # Ensure json is imported

class ContractAnalyzer:
    """
    Orchestrates the entire contract analysis process, from parsing to chatbot interaction.
    """
    def __init__(self):
        self.llm_integration = AzureLLM()
        self.parser = ContractParser(self.llm_integration)
        self.parsed_contract_data = {}
        self.contract_text = ""

    def load_and_analyze_contract(self, contract_text: str):
        """
        Loads the contract text and performs all initial analyses.
        """
        self.contract_text = contract_text
        if not contract_text:
            return {"error": "No contract text provided for analysis."}

        print("Extracting key information...")
        self.parsed_contract_data["key_information"] = self.parser.extract_key_information(contract_text)

        print("Identifying risks...")
        self.parsed_contract_data["risks"] = self.parser.identify_risks(contract_text)

        print("Summarizing clauses...")
        self.parsed_contract_data["clause_summaries"] = self.parser.summarize_clauses(contract_text)

        print("Getting overall score...")
        self.parsed_contract_data["overall_score"] = self.parser.get_overall_score(contract_text)

        return self.parsed_contract_data

    def chat_with_contract(self, query: str) -> str:
        """
        Allows interaction with the contract analysis via a chatbot.
        The chatbot will have access to the raw contract text and the generated insights.
        """
        if not self.contract_text:
            return "Please load and analyze a contract first."

        # Combine raw contract and parsed data for context
        context_for_chatbot = f"""
        Contract Document:
        ---
        {self.contract_text}
        ---

        Extracted Key Information:
        {json.dumps(self.parsed_contract_data.get('key_information', {}), indent=2)}

        Identified Risks:
        {self.parsed_contract_data.get('risks', 'No risks identified.')}

        Clause Summaries:
        {self.parsed_contract_data.get('clause_summaries', 'No summaries generated.')}

        Overall Score:
        {self.parsed_contract_data.get('overall_score', 'No score generated.')}

        User Query: {query}
        """

        response = self.llm_integration.generate_response(
            system_message_content=CHATBOT_SYSTEM_PROMPT,
            user_message_content=context_for_chatbot
        )
        return response