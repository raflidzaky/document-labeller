import streamlit as st
import display
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import text_parser, process_docs, text_corpora

def main():
    # Display basic functionalities
    display.display_page()
    display.guide()

    # Upload the files
    file = display.upload_button()

    if file:
    # If the image is being uploaded, we ask user to click predict button
        process_button = display.summarize_button()

        # Ir the predict button is done clicked, then start doing inference
        if process_button:
            st.write("Wait, we are recognizing what is this document about!")

            # Make a progress bar for each step
            # Initializing with 0
            # And progress status
            progress_bar = st.progress(0)
            status_text = st.empty()

            pdf_text = text_parser.extract_text_from_pdf(pdf_file=file)
            if pdf_text:
                status_text.text("Your file is already parsed, proceeding with prediction...")
                progress_bar.progress(25)  # Update progress

            # Run prediction
            returns = process_docs.simplify_docs(sentence=pdf_text)
            keywords = [item[0] for item in returns]
            keywords_str = ', '.join(keywords)

            if keywords_str:
                progress_bar.progress(100)  # Complete progress
                st.write(f'Your document is all related to these words:')
                st.write(keywords_str)
        
if __name__ == "__main__":
    text_corpora.download_corpora()
    main()