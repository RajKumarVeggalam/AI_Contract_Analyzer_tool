# src/contract_parser.py
from src.llm_integration import AzureLLM
from src.prompt_templates import (
    GENERAL_CONTRACT_ANALYSIS_SYSTEM_PROMPT,
    EXTRACT_KEY_INFO_PROMPT,
    CLAUSE_SUMMARY_PROMPT,
    RISK_IDENTIFICATION_PROMPT,
    OVERALL_SCORE_PROMPT
)
import json

class ContractParser:
    """
    Parses a contract document to extract key information, identify risks,
    and generate summaries using an LLM.
    """
    def __init__(self, llm_integration: AzureLLM):
        self.llm = llm_integration

    def extract_key_information(self, contract_text: str) -> dict:
        """
        Extracts structured key information from the contract.
        """
        user_message = EXTRACT_KEY_INFO_PROMPT.format(contract_text=contract_text)
        response = self.llm.generate_response(
            system_message_content=GENERAL_CONTRACT_ANALYSIS_SYSTEM_PROMPT,
            user_message_content=user_message
        )
        # Attempt to parse as JSON if the LLM is good at generating it
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            print("Warning: LLM did not return perfect JSON for key info. Returning raw text.")
            return {"raw_response": response} # Fallback to raw text

    def identify_risks(self, contract_text: str) -> str:
        """
        Identifies potential risks in the contract.
        """
        user_message = RISK_IDENTIFICATION_PROMPT.format(contract_text=contract_text)
        response = self.llm.generate_response(
            system_message_content=GENERAL_CONTRACT_ANALYSIS_SYSTEM_PROMPT,
            user_message_content=user_message
        )
        return response

    def summarize_clauses(self, contract_text: str) -> str:
        """
        Generates summaries for key clauses.
        """
        user_message = CLAUSE_SUMMARY_PROMPT.format(contract_text=contract_text)
        response = self.llm.generate_response(
            system_message_content=GENERAL_CONTRACT_ANALYSIS_SYSTEM_PROMPT,
            user_message_content=user_message
        )
        return response

    def get_overall_score(self, contract_text: str) -> str:
        """
        Calculates and justifies an overall contract score.
        """
        user_message = OVERALL_SCORE_PROMPT.format(contract_text=contract_text)
        response = self.llm.generate_response(
            system_message_content=GENERAL_CONTRACT_ANALYSIS_SYSTEM_PROMPT,
            user_message_content=user_message
        )
        return response