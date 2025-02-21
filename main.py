from fastapi import FastAPI, Request, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from github_tracker import TrackerPayload, check_repo

app = FastAPI()

# Enable CORS for public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/integration.json")
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {
                "created_at": "2025-02-19",
                "updated_at": "2025-02-19"
            },
            "descriptions": {
                "app_name": "GitHub Fork Event Tracker",
                "app_description": "A monitoring system that alert user about details of the fork event on a github repository.",
                "app_url": base_url,
                "app_logo": "https://www.hostpapa.com/blog/app/uploads/2022/07/Why-You-Need-An-Application-Performance-Monitoring-Tool-header.jpg",
                "background_color": "#fff"
            },
            "integration_category": "Monitoring & Logging",
            "integration_type": "interval",
            "is_active": False,
            "key_features": [
                "Track a github repository for fork event",
                "Alert the original repo owner of the event providing the visitor name, time of request, and visitors forked url"
            ],
            "settings": [
                {"label": "repo_name", "type": "text", "required": True, "default": "username/repo"},
                {"label": "interval", "type": "text", "required": True, "default": "* * * * *"}
            ],
            "tick_url": f"{base_url}/tick",
            "target_url": ""
        }
    }


@app.post("/tick", status_code=200)
def monitor(payload: TrackerPayload, background_tasks: BackgroundTasks):
    try:
        # Add the task to the background tasks queue
        background_tasks.add_task(check_repo, payload)
        return {"message": "Task added to background tasks"}
    except Exception as e:
        # Log the error and return a 500 Internal Server Error response
        print(f"Error adding task to background tasks: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    