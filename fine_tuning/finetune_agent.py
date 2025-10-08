
from google.colab import drive
import os


drive.mount('/content/drive')

project_path = '/content/drive/My Drive/AGENT_DEV_DRIVE'

os.chdir(project_path)

print(f"Current working directory: {os.getcwd()}")

from huggingface_hub import login
from pyngrok import ngrok
import os

print("Please enter your Hugging Face token:")
login()

NGROK_AUTHTOKEN = "33mgAzkVXyc2q8xwrZ7mcAwF9n1_6RNvVPEtm9a3apEWD16yZ"  # <--- PASTE YOUR NGROK AUTHTOKEN HERE
os.environ['NGROK_AUTHTOKEN'] = NGROK_AUTHTOKEN

ngrok.kill()

import uvicorn
from pyngrok import ngrok
import asyncio
import nest_asyncio

# This is needed to run an asyncio event loop within Colab's existing loop
nest_asyncio.apply()

# This function will start the ngrok tunnel and print the public URL
def setup_ngrok_tunnel():

    public_url = ngrok.connect(8000)
    print("--- YOUR LIVE BACKEND IS READY ---")
    print(f"Public URL: {public_url}")
    print("You can now use this URL in your frontend application.")
    print("---------------------------------")
    return public_url

# This function runs the uvicorn server
def run_uvicorn_server():

    uvicorn.run("agent_backend.main:app", host="0.0.0.0", port=8000)

from threading import Thread

server_thread = Thread(target=run_uvicorn_server)
server_thread.start()

import time
time.sleep(5)

setup_ngrok_tunnel()