import azure.functions as func
from azure.storage.blob import BlobClient
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    filename = req.params.get('file')
    blob = BlobClient.from_connection_string(
        conn_str=os.getenv("STORAGE_CONNECTION_STRING"),
        container_name="userfiles",
        blob_name=filename
    )
    
    download_stream = blob.download_blob()
    return func.HttpResponse(
        download_stream.readall(),
        mimetype="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
