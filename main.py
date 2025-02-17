from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
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

# Load Slack Webhook URL from environment variables
# SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

@app.post("/github-webhook")
async def github_webhook(request: Request):
    try:
        payload = await request.json()

        # Check if it's a fork event
        if "forkee" in payload:
            repo_name = payload["repository"]["full_name"]
            forked_by = payload["forkee"]["owner"]["login"]
            fork_url = payload["forkee"]["html_url"]

            message = f"🔄 *{forked_by}* just forked *{repo_name}*! 🎉\n🔗 {fork_url}"
            # # Send notification to Slack
            # async with httpx.AsyncClient() as client:
            #     response = await client.post(SLACK_WEBHOOK_URL, json=slack_message)
            return Response(content=json.dumps({"message": message }), status_code=200, media_type="application/json")
            # return Response(content=json.dumps({"status": "Notification sent"}), status_code=int(response.status_code), media_type="application/json")
        else:
            return Response(content=json.dumps({"status": "No forked event!"}), status_code=400, media_type="application/json")
    except Exception as e:
        return Response(content=json.dumps({"error": str(e)}), status_code=500, media_type="application/json")
        