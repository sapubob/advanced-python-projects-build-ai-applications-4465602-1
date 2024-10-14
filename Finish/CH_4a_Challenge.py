# Import necessary libraries
import streamlit as st  # Streamlit for building interactive web apps
import requests  # Requests library for sending HTTP requests

# Set the FastAPI endpoint URL where the file will be uploaded
FASTAPI_URL = "http://127.0.0.1:8000/uploadFile"

# Function to handle file upload
def upload_file(file):
    # Prepare the file to be sent in a POST request to the FastAPI backend
    files = {'data_file': file}
    
    # Send the POST request to the FastAPI server with the file
    response = requests.post(FASTAPI_URL, files=files)
    
    # Check the response status code to ensure the upload was successful
    if response.status_code == 200:
        # If successful, display a success message and the JSON response
        st.success("File uploaded successfully!")
        st.json(response.json())  # Display the JSON response in the app
    else:
        # If an error occurs, display an error message with the response text
        st.error("Error during file upload: " + response.text)

# Streamlit UI setup
# Configure the page with a title, icon, and layout
st.set_page_config(page_title="Challenge", page_icon="📕", layout="wide")

# Streamlit file uploader widget
# Allows the user to select a file of specified types (docx, csv, txt, pdf)
uploaded_file = st.file_uploader("Choose a file to upload", type=["docx", "csv", "txt", "pdf"])

# If a file is selected and the "Upload" button is clicked
if uploaded_file is not None:
    if st.button("Upload"):
        # Call the function to upload the selected file
        upload_file(uploaded_file)
        
# Command to run the Streamlit app
# streamlit run Begin/CH_4a_Challenge.py
