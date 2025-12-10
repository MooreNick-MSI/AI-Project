from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Instantiate object
app = FastAPI()

# Enables front end to call API from a different port
app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["*"], 
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Pydantic model for requests payload
class Query(BaseModel):
    query : str

# Post endpoint
@app.post("/ask")
def ask(data: Query):
    # print to confirm it was received properly
    print("Received from HTML:", data.query)
    # return value -> what is displayed on HTML
    return {"reply" : f"Server received: {data.query}"}

# ------------------------------------------------------------------------------
# This is all for a POC, HTML front end -> Python app -> HTML
# Modifications needed for Amazon Bedrock use case
# Changes will be made to this file
# Need to import boto3 & json
# boto3.client object needs to be instantiated
# something like this will need to be added to the ask()
# response = boto3.client.invoke_model(modelId = "XXXX", body = json.dumps({DATA}))
# output = json.loads(response)
# reply = output["INDEX-FOR-DATA"]
# -------------------------------------------------------------------------------