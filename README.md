# project_ai_engineering_az_01

This project demonstrates how to build serverless APIs and automate
workflows in **Microsoft Azure** while leveraging **OpenAI** models.  It
includes code for deploying Azure Functions that interact with the OpenAI
API to perform tasks such as text generation, summarisation or question
answering.

## What’s inside

* **Azure Functions** written in Python that call the OpenAI API.  These
  functions can be triggered via HTTP requests or timers and return AI‑generated
  responses.
* Infrastructure‑as‑code scripts (e.g. Azure CLI or Bicep) for deploying
  the functions and configuring environment variables.
* Examples illustrating how to secure your functions and manage API keys.

## Technologies used

* **Azure Functions** – serverless compute platform.  Documentation:
  <https://learn.microsoft.com/azure/azure-functions/>
* **OpenAI API** – provides access to generative AI models.  Documentation:
  <https://platform.openai.com/docs>
* **Python** – the runtime for the function apps.
