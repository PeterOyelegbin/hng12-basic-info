# GitHub Fork Alert
This project is a FastAPI-based integration that listens for fork events on your GitHub repositories and sends a notification to a Slack channel when a repository is forked.

---

## Features
- Listens for GitHub fork events via a webhook
- Sends a Slack notification when a repository is forked
- Uses FastAPI for handling incoming GitHub webhook requests
- Asynchronous HTTP requests using httpx

---

## Technology Stack
- **FastAPI** (Web framework)
- **httpx** (Async HTTP requests)
- **Uvicorn** (ASGI server for FastAPI)
- **GitHub Webhook** (Repository Webhook)

---

## Prerequisites
1. Create a Slack Incoming Webhook
   - Go to Slack API Webhooks and create an Incoming Webhook.
   - Copy the provided Webhook URL (e.g., https://hooks.slack.com/services/T000/B000/XYZ).

2. Set Up a GitHub Webhook
   - Navigate to Settings > Webhooks in your repository.
   - Click "Add Webhook" and enter your FastAPI server's public URL.
   - Set the Content Type to application/json.
   - Select "Just the fork event" and save.

---

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. Set Environment Variables
   Create a .env file or export the variable directly:
   ```bash
   export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/T000/B000/XYZ"
   ```

---

## Running the API Locally
1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
2. **Access the API documentation:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for an interactive Swagger UI.

---

## API Endpoints
- **Endpoint:** `POST /github-webhook`
- **Example Request:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/github-webhook"
  ```
