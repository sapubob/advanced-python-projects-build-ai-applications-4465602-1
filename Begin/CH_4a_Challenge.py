# Import necessary libraries


# Set the FastAPI endpoint URL where the file will be uploaded
FASTAPI_URL = "http://127.0.0.1:8000/uploadFile"

# Function to handle file upload
def upload_file(file):
    # Prepare the file to be sent in a POST request to the FastAPI backend
    files = {'data_file': file}
    
    # Send the POST request to the FastAPI server with the file
    
    
    # Check the response status code to ensure the upload was successful
    if 
        # If successful, display a success message and the JSON response
        
    else:
        # If an error occurs, display an error message with the response text
        

# Streamlit UI setup
# Configure the page with a title, icon, and layout


# Streamlit file uploader widget
# Allows the user to select a file of specified types (docx, csv, txt, pdf)


# If a file is selected and the "Upload" button is clicked
if uploaded_file is not None:
    if st.button("Upload"):
        # Call the function to upload the selected file
        
        
# Command to run the Streamlit app
# streamlit run Begin/CH_4a_Challenge.py
