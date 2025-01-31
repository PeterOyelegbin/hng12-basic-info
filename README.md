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
4. Open a web browser and navigate to `http://127.0.0.1:8000/` to test the API.


## API Documentation
### Endpoint
* `GET /`: Returns the email, current datetime in ISO 8601 format, and github url.

### Request/Response Format
* Request: None
* Response:
  ```
  {
      "email": "peteroyelegbin@gmail.com",
      "current_datetime": "2025-01-31T21:12:02.158314+00:00",
      "github_url": "https://github.com/PeterOyelegbin/hng12-basic-info"
  }
  ```
