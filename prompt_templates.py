# src/prompt_templates.py

# System prompt for general contract analysis
GENERAL_CONTRACT_ANALYSIS_SYSTEM_PROMPT = """
You are an expert contract analyzer. Your task is to meticulously review legal and business contracts,
extract key information, identify risks, and summarize clauses.
Provide concise, accurate, and structured responses.
"""

# Prompt for extracting key information from a contract
EXTRACT_KEY_INFO_PROMPT = """
From the following contract document, extract the following key information:
1. Parties involved (Client and Service Provider names)
2. Effective Date
3. Total Fee
4. Payment Schedule (amounts and trigger events)
5. Project Kickoff Date
6. Milestone 1 (description and date)
7. Milestone 2 (description and date)
8. Milestone 3 (description and date)
9. Completion Date
10. Scope of Services (list of services)
11. Deliverables (list of deliverables)
12. Termination Clause notice periods (for Client and Service Provider)
13. Limitation of Liability cap
14. Intellectual Property Rights (who owns deliverables)

Present the information in a clear, structured format, e.g., JSON or bullet points.
If a piece of information is not explicitly present, state 'Not specified'.

Contract Document:
---
{contract_text}
---
"""

# Prompt for identifying potential contract risks
RISK_IDENTIFICATION_PROMPT = """
Analyze the following contract document for potential risks based on the following criteria:
- Liability limitations and exclusions for indirect or consequential damages.
- Termination clauses with notice requirements (assess if balanced).
- Intellectual Property ownership and usage rights (identify who retains IP).
- Payment terms and late fees (assess fairness and clarity).
- Confidentiality obligations and permitted use of anonymized data (identify any exceptions).
- Project scope and timeline adjustments due to technical complexity.
- Force Majeure clause implications.
- Indemnity clause implications.

For each identified risk, provide:
1. A brief description of the risk.
2. The relevant clause or section from the contract (if applicable).
3. A risk level (High, Medium, Low) and a brief justification.
4. Suggestions for alternative wording or best-practice clauses to mitigate the risk.

Present the identified risks in a structured format.

Contract Document:
---
{contract_text}
---
"""

# Prompt for creating clause summaries
CLAUSE_SUMMARY_PROMPT = """
Summarize the key clauses of the following contract document. For each main section (e.g., Scope of Services, Deliverables, Payment Terms, Termination, Liability), provide a concise summary (1-3 sentences) highlighting its core intent and any critical details.

Contract Document:
---
{contract_text}
---
"""

# Prompt for overall contract score (simplified for hackathon)
OVERALL_SCORE_PROMPT = """
Based on the completeness, clarity, and balance of the clauses in the following contract, provide an overall contract score between 1 and 100, where 100 is excellent. Justify your score briefly, mentioning strong points and areas for improvement.

Contract Document:
---
{contract_text}
---
"""

# Prompt for an integrated chatbot
CHATBOT_SYSTEM_PROMPT = """
You are an intelligent chatbot designed to answer questions about a legal contract.
You have access to the full contract text and various analyses of it.
Answer user questions directly and concisely based *only* on the provided contract and its analysis.
If the information is not present, state that you don't have enough information.
"""