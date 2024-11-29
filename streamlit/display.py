import streamlit as st

'''
    This module has several functions that provide utilities to support basic landing page,
    as users entered the web. Several utilities:
    1. What page that users currently in
    2. Guide for users 
    3. Upload file button, that users could upload to
    4. Button to summarize the file
'''

def display_page():
    # Func for landing page introduction
    st.title("Welcome to Document Metadata Labeller!")
    st.write("❓ This site provide a service for you to recognize what keyword that describe the documents!")
    st.write("✅ You can upload all of your text-in-PDF file!")
    st.write('---'*5)
    st.write('  ')
    st.write('  ')

def guide():
    # Func for user guide
    st.write('❗ Just upload a random text PDF')
    st.write('❗ The result of this web is working optimal on English files. \nIf you use other language, it might work unexpectedly')
    st.write(' ')
    
def upload_button():
    file = st.file_uploader('Upload image here', type=['pdf'],
                             accept_multiple_files=False,
                             key='up145'
                            )
    # Since I want pass a value for the model, this function
    # will return the image that is being uploaded.
    # Also, this image will be displayed in display_image.py module.    
    return file

def summarize_button():
    st.write("Do you want to know what is this file about?")
    # Since I want the predict button returns any value after "clicking action"
    # I make the st.button as return.
    # Hence, this value will be passed as a logic to trigger steps to predict model.
    return st.button("Yes, I want!", key="summarize_button")