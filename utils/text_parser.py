import fitz  
import io
import PyPDF2

def extract_text_from_pdf(pdf_file):
    '''
        This function has several logic:
        1. Making sure user uploads a .PDF
        2. Extract the .PDF 

        Since streamlit returns any file that is being uploaded as a BytesIO object,
        I need a library that able to receive it in memory (instead traditional absolute link).

        After processing and extract the text, it will return a single string variable containing
        paragrahps of the file. 
    '''
    # Make sure it store file name if user upload any 
    # This is used to make sure the file is on .PDF form (for example 'xyz.pdf')
    file_name = pdf_file.name if hasattr(pdf_file, 'name') else ""
    if not file_name.lower().endswith('.pdf'):
        raise ValueError("The uploaded file is not a PDF")
    
    # Open the PDF file directly using fitz from the BytesIO object
    try:
        pdf_stream = io.BytesIO(pdf_file.read())
        
        # Open the PDF using PyPDF2
        reader = PyPDF2.PdfReader(pdf_stream)
        text = ""
        
        # Extract text from each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text
    except Exception as e:
        raise ValueError(f"Error while processing the PDF: {e}")

