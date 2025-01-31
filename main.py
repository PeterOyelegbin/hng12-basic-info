from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
import json

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/basic-info")
async def home():
    current_datetime = datetime.now(timezone.utc).isoformat()
    response = {
        "email": "peteroyelegbin@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/PeterOyelegbin/hng12-basic-info"
    }
    return Response(content=json.dumps(response), media_type="application/json")
