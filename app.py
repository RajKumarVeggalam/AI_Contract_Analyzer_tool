# src/app.py
import streamlit as st
import os
from utils.pdf_reader import extract_text_from_pdf
from src.contract_analyzer import ContractAnalyzer
import json # for pretty printing JSON outputs

st.set_page_config(layout="wide", page_title="Contract Analyzer Tool")

st.title("📄 Contract Analyzer Tool")
st.markdown("Automate contract review, risk assessment, and insight generation.")

# Initialize ContractAnalyzer (and LLM)
@st.cache_resource
def get_analyzer():
    try:
        return ContractAnalyzer()
    except ValueError as e:
        st.error(f"Configuration error: {e}. Please ensure your .env file is correctly set up.")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred during analyzer initialization: {e}")
        st.stop()

analyzer = get_analyzer()

uploaded_file = st.sidebar.file_uploader("Upload a Contract (PDF)", type="pdf")

if uploaded_file:
    st.sidebar.success("File uploaded successfully!")
    with st.spinner("Extracting text from PDF..."):
        # Pass the uploaded_file object directly to the function
        contract_text = extract_text_from_pdf(uploaded_file)

    if contract_text:
        st.subheader("Document Preview (First 1000 characters)")
        st.text_area("Contract Content", contract_text[:1000] + "...", height=150)

        # Only analyze if a button is clicked, prevents re-analysis on every interaction
        if st.sidebar.button("Analyze Contract"):
            with st.spinner("Analyzing contract using Azure AI... This may take a few minutes."):
                analysis_results = analyzer.load_and_analyze_contract(contract_text)

            if "error" in analysis_results:
                st.error(analysis_results["error"])
            else:
                st.session_state["analysis_results"] = analysis_results
                st.session_state["contract_text"] = contract_text # Store for chatbot

                st.success("Contract Analysis Complete!")

                st.subheader("🚀 Key Information")
                key_info = st.session_state["analysis_results"].get("key_information", {})
                if isinstance(key_info, dict) and "raw_response" in key_info:
                    st.text_area("Raw Key Information Output (LLM couldn't format perfectly)", key_info["raw_response"], height=300)
                else:
                    st.json(key_info)

                st.subheader("⚠️ Identified Risks")
                st.markdown(st.session_state["analysis_results"].get("risks", "No risks identified."))

                st.subheader("📜 Clause Summaries")
                st.markdown(st.session_state["analysis_results"].get("clause_summaries", "No summaries generated."))

                st.subheader("📊 Overall Score")
                st.markdown(st.session_state["analysis_results"].get("overall_score", "No score calculated."))
    else:
        st.sidebar.error("Failed to extract text from the PDF. Please check the file's content.")

# Chatbot Interface
if "analysis_results" in st.session_state and st.session_state["analysis_results"]:
    st.markdown("---")
    st.subheader("💬 Chat with your Contract")
    st.info("Ask questions about the contract you just analyzed.")

    user_query = st.text_input("Your question:", key="chatbot_input")

    if user_query:
        with st.spinner("Thinking..."):
            chatbot_response = analyzer.chat_with_contract(user_query)
        st.write("---")
        st.markdown(f"**Chatbot:** {chatbot_response}")

elif uploaded_file and not contract_text:
    st.error("Please upload a valid PDF and ensure text can be extracted.")
else:
    st.info("Upload a contract PDF in the sidebar to begin analysis.")