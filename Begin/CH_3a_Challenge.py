from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from datetime import datetime
import boto3
import awswrangler as wr
from pymongo import MongoClient
import pymongo

# Initialize FastAPI app
app = FastAPI()

# Initialize S3 boto3 session and MongoDB client (adjust your connection as needed)
aws_s3 = boto3.Session(
    aws_access_key_id="AKIARMZIQE2E2NFRGHXL",
    aws_secret_access_key="1jbz3wTw4sWvSNGxYiZyqpbb3RhglW8EfbtJOyHs",
    region_name="us-east-2"
)

# install mongo db in codespace using below commands
# sudo apt-get update
# sudo apt-get install -y mongodb

# start the Database
# sudo service mongodb start

client = MongoClient("mongodb://localhost:27017/")
db = client["local"]

# Define your S3 bucket and path
S3_BUCKET = "docchat"
S3_PATH = "downloads/"

@app.post("/uploadFile")
async def uploadtos3(data_file: UploadFile):
    """
    Uploads a file to Amazon S3 storage and stores metadata in MongoDB.

    This route allows users to upload a file, which is saved temporarily, uploaded to Amazon S3,
    and then removed from the local file system. It returns the filename and S3 file path
    in the response JSON, while storing file metadata in MongoDB.

    Args:
        data_file (UploadFile): The file to be uploaded.

    Returns:
        JSONResponse: A JSON response containing the filename, file size, upload time, and S3 file path.

    Raises:
        HTTPException: If the file specified in `data_file` is not found (HTTP status code 404).
    """
    try:
        file_name = data_file.filename.split("/")[-1]
        
        # Save the file temporarily to the local file system
        with open(f"{file_name}", "wb") as out_file:
            content = await data_file.read()  # async read
            out_file.write(content)  # write to disk
        
        # Get the file size
        file_size = os.path.getsize(file_name)
        
        # Get the upload timestamp
        upload_time = str(datetime.now())
        
        # Upload file to AWS S3
        wr.s3.upload(
            local_file=file_name,
            path=f"s3://{S3_BUCKET}/{S3_PATH}{file_name}",
            boto3_session=aws_s3,
        )
        
        # Remove the local file after upload
        os.remove(file_name)

        # Prepare metadata to store in MongoDB
        metadata = {
            "filename": file_name,
            "file_size": file_size,
            "upload_time": upload_time,
            "s3_path": f"s3://{S3_BUCKET}/{S3_PATH}{file_name}",
        }

        # Insert file metadata into MongoDB
        result = db["file_metadata"].insert_one(metadata)
        
        # Print details in the terminal
        print(f"File '{file_name}' uploaded successfully.")
        print(f"Size: {file_size} bytes")
        print(f"Upload Time: {upload_time}")
        print(f"MongoDB Insert Status: {result.acknowledged}")

        # Return response
        response = {
            "filename": file_name,
            "file_size": file_size,
            "upload_time": upload_time,
            "file_path": f"s3://{S3_BUCKET}/{S3_PATH}{file_name}",
            "mongo_insert_status": result.acknowledged,
        }

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    
    except Exception as e:
        print(f"Error during file upload: {e}")
        raise HTTPException(status_code=500, detail="Error during file upload")

    return JSONResponse(content=response)
