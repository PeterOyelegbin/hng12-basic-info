# Number Classification API
The **Number Classification API** is a FastAPI-based web service that analyzes a given integer and returns various mathematical properties along with a fun fact about the number.

---

## Features
- Determines if a number is **prime**
- Checks if a number is **perfect**
- Identifies **Armstrong numbers**
- Classifies the number as **odd or even**
- Computes the **sum of digits**
- Fetches a **fun fact** from the Numbers API
- CORS enabled for cross-origin requests

---

## Technology Stack
- **FastAPI** (Web framework)
- **httpx** (Async HTTP requests)
- **Uvicorn** (ASGI server for FastAPI)
- **Math library** (Mathematical operations)

---

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
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
- **Endpoint:** `GET /api/classify-number?number=<integer>`
- **Request Parameters:**
  - `number` (integer, required) - The number to be analyzed.
- **Example Request:**
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
  ```
- **Example Response:**
  ```json
  {
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }
  ```
