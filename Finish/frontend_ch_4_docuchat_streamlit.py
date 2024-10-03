oiimport streamlit as st
import requests

# Set the FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/uploadFile"

def upload_file_to_backend(file):
    files = {'data_file': file}
    response = requests.post(FASTAPI_URL, files=files)
    
    if response.status_code == 200:
        st.success("File uploaded successfully!")
        st.json(response.json())
    else:
        st.error("Error during file upload: " + response.text)

# Streamlit UI
st.title("File Uploader")

uploaded_file = st.file_uploader("Choose a file to upload", type=["csv", "txt", "pdf"])

if uploaded_file is not None:
    if st.button("Upload"):
        upload_file_to_backend(uploaded_file)
