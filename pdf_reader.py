# utils/pdf_reader.py
from pypdf import PdfReader

def extract_text_from_pdf(pdf_file) -> str:
    """
    Extracts all text from an uploaded PDF file-like object.

    Args:
        pdf_file: A file-like object (e.g., from Streamlit's file_uploader) of a PDF.

    Returns:
        str: The concatenated text content of the PDF.
    """
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

if __name__ == "__main_":
    # This block is for direct testing if needed, but not part of the core app logic
    # For testing, you would need to simulate a file upload.
    print("This module is designed to be imported. For testing, simulate a file object.")