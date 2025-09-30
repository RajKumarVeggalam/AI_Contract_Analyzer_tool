📄 AI Contract Analyzer Tool

An AI-powered contract analysis platform that automates legal document review using Azure OpenAI + LangChain.
The tool extracts key details, flags risks, generates clause summaries, assigns an overall fairness score, and enables an interactive chatbot for Q&A over uploaded contracts.

✨ Features

📑 Contract Upload – Upload any PDF contract directly via the Streamlit UI.
🔍 Key Information Extraction – Parties, dates, payment milestones, IP rights, deliverables, termination clauses.
⚠️ Risk Identification – Detects liability gaps, unfair terms, confidentiality risks, and more (with High/Medium/Low severity).
📜 Clause Summaries – Simplified summaries of legal clauses for non-legal stakeholders.
📊 Overall Contract Score – Fairness, balance, and completeness scored 1–100 with justification.

💬 Chat with the Contract – Ask natural questions like:
“Who owns the intellectual property?”
“What are the payment milestones?”
“Can the client terminate early?”    

⚡ Tech Stack

Frontend: Streamlit
LLM Orchestration: LangChain
LLM Backend: Azure OpenAI Service
PDF Processing: PyPDF
Token Management: Tiktoken

🧪 How to Use

Upload a contract PDF in the sidebar.
Preview the extracted text.
Click Analyze Contract → Key info, risks, summaries, and score appear.
Use the Chat with Contract section to ask follow-up questions.

📈 Future Improvements

RAG-powered retrieval for multi-document handling.
Dashboard view for contract comparison (SoW vs MSA).
Multi-user access with role-based permissions.
Integration with compliance checklists (e.g., GDPR, HIPAA).
