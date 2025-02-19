from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from pathlib import Path
import httpx, json, os

app = FastAPI()

# Enable CORS for public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load JSON data from file
def load_app_data():
    data_path = Path(__file__).parent / "app_data.json"
    with open(data_path, "r") as file:
        return json.load(file)
    
# Function to get the value of a specific label from settings
def get_setting_value(data, label):
    for setting in data["data"]["settings"]:
        if setting["label"] == label:
            return setting["default"]
    return None  # Return None if the label is not found

# Configuration    
GITHUB_REPO = get_setting_value(load_app_data(), "repo_name")  # Target github repo
# CHANNEL_WEBHOOK = get_setting_value(load_app_data(), "telex_channel_webhook")  # Telex channel URL

# GITHUB_API_URL = f"https://api.github.com/users/PeterOyelegbin/events"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/forks"

latest_forks = set()

# Base endpoint
@app.get("/")
def home():
    return {"message": "GitHub Fork Event Tracker Active"}


# Endpoint to serve the JSON data
@app.get("/app-info")
async def get_app_info():
    return load_app_data()


# Endpoint to triger monitoring
@app.get("/check-repo")
async def check_repo():
    global latest_forks
    async with httpx.AsyncClient() as client:
        response = await client.get(GITHUB_API_URL)
    
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch forks")
        
        forks = response.json()
        
        new_forks = []
        
        for fork in forks:
            fork_id = fork["id"]
            if fork_id not in latest_forks:
                latest_forks.add(fork_id)
                new_forks.append({
                    "forked_by": fork["owner"]["login"],
                    "repo_name": fork["name"],
                    "forked_at": fork["created_at"],
                    "fork_url": fork["html_url"]
                })

        if new_forks:
            # Convert the new_forks list of dictionaries into a formatted string
            message = "New forks detected:\n"
            for fork in new_forks:
                message += (
                    f"🔄Repo: {fork['repo_name']}\n"
                    f"Forked by: {fork['forked_by']}\n"
                    f"Forked at: {fork['forked_at']}\n"
                    f"🎉URL: {fork['fork_url']}\n\n"
                )
            # await send_alert(new_forks)
            return {"message": "Fork check completed", "new_forks": message}
        else:
            return {"message": "No new forks detected"}
        

# async def send_alert(fork_data):
#     # Convert the fork_data list of dictionaries into a formatted string
#     message = "New forks detected:\n"
#     for fork in fork_data:
#         message += (
#             f"🔄Repo: {fork['repo_name']}\n"
#             f"Forked by: {fork['forked_by']}\n"
#             f"Forked at: {fork['forked_at']}\n"
#             f"🎉URL: {fork['fork_url']}\n\n"
#         )
#     payload = {
#         "event_name": "forked",
#         "message": message,
#         "status": "success",
#         "username": "GitHub Fork Monitor",
#     }
#     async with httpx.AsyncClient() as client:
#         response = await client.post(CHANNEL_WEBHOOK, json=payload)
#         if response.status_code != 202:
#             print("Failed to send data to Telex channel", response.text)
#         else:
#             print("Successfully sent data to Telex channel")
