import azure.functions as func
from azure.storage.blob import ContainerClient
import os
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    container = ContainerClient.from_connection_string(
        conn_str=os.getenv("STORAGE_CONNECTION_STRING"),
        container_name="userfiles"
    )
    
    files = [blob.name for blob in container.list_blobs()]
    return func.HttpResponse(json.dumps(files), mimetype="application/json")
