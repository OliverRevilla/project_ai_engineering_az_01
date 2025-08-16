import azure.functions as func
import logging
import json
from dotenv import load_dotenv
import os

# Explicitly load .env from the app root directory
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path=env_path)

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_type = os.getenv("OPENAI_API_TYPE")
openai_api_base = os.getenv("OPENAI_API_BASE")

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="OpenAI_trigger/greeting", methods=["GET"])
@app.text_completion_input(
    arg_name="name",
    prompt="Please provide your name for a personalized greeting.",
    max_tokens=50,
    temperature=0.5,
    chat_model="gpt-4o-mini-2024-07-18"
)
def OpenAI_trigger(req: func.HttpRequest, response:str) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    response_json = json.loads(response)
    return func.HttpResponse(response_json['content'], status_code=200)