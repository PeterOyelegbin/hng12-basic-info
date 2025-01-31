# Basic Info API
A simple API that returns an intern email, current datetime in ISO 8601 format, and github repo url in JSON format.

## Setup
1. Clone the repository
    ```bash
    git clone https://github.com/PeterOyelegbin/hng12-basic-info.git
    ```
2. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Run the API
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```
4. Open a web browser and navigate to `http://localhost:8000/` to test the API.


## API Documentation
### Endpoint
* `GET /`: Returns the current datetime in ISO 8601 format.

### Request/Response Format
* Request: None
* Response: JSON object with a single key-value pair: `"current_datetime": "2025-01-30T09:30:00Z"`

## Deployment
The API is designed to be deployed on a cloud platform or a containerization service like Docker. Ensure that the API has a fast response time (< 500ms).
