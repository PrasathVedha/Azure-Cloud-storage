import azure.functions as func
from azure.storage.blob import BlobClient
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    file = req.get_body()
    filename = req.headers.get('x-ms-blob-name')
    
    blob = BlobClient.from_connection_string(
        conn_str=os.getenv("STORAGE_CONNECTION_STRING"),
        container_name="userfiles",
        blob_name=filename
    )
    
    blob.upload_blob(file)
    return func.HttpResponse("OK", status_code=200)
