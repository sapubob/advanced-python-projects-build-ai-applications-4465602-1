from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from datetime import datetime
import boto3
import awswrangler as wr
from pymongo import MongoClient
import pymongo

# Initialize FastAPI app

# Initialize S3 boto3 session and MongoDB client (adjust your connection as needed)
aws_s3 = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name=""
)

# install mongo db in codespace using below commands
# sudo apt-get update
# sudo apt-get install -y mongodb

# start the Database
# sudo service mongodb start

client = MongoClient("mongodb://localhost:27017/")
db = client["local"]

# Define your S3 bucket and path
S3_BUCKET = ""
S3_PATH = ""

@app.post("/uploadFile")
async def uploadtos3(data_file: UploadFile):

    try:
        file_name = data_file.filename.split("/")[-1]
        
        # Save the file temporarily to the local file system

        
        # Get the file size
        file_size = os.path.getsize(file_name)
        
        # Get the upload timestamp
        upload_time = str(datetime.now())
        
        # Upload file to AWS S3
       
        
        # Remove the local file after upload
 

        # Prepare metadata to store in MongoDB
        metadata = {
            "filename": file_name,
            "file_size": file_size,
            "upload_time": upload_time,
            "s3_path": f"s3://{S3_BUCKET}/{S3_PATH}{file_name}",
        }

        # Insert file metadata into MongoDB
        result = db["file_metadata"].insert_one(metadata)
        

        # Return response
        response = {
            "filename": file_name,
            "file_size": file_size,
            "upload_time": upload_time,
            "file_path": f"s3://{S3_BUCKET}/{S3_PATH}{file_name}",
            "mongo_insert_status": result.acknowledged,
        }

    except FileNotFoundError:

    
    except Exception as e:
        print(f"Error during file upload: {e}")
        raise HTTPException(status_code=500, detail="Error during file upload")

    return JSONResponse(content=response)
        print(f"Error during file upload: {e}")
        raise HTTPException(status_code=500, detail="Error during file upload")

    return JSONResponse(content=response)
