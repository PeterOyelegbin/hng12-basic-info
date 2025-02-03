from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx, json
from utils import is_prime, is_perfect, get_number_properties

app = FastAPI()

# Enable CORS for public access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API for fun facts
NUMBERS_API_URL = "http://numbersapi.com/{}"

async def get_fun_fact(n: int) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{NUMBERS_API_URL.format(n)}/math")
        if response.status_code == 200:
            return response.text.strip()
        return "No fun fact available."


@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="Enter number to classify")):
    try:
        number = int(number)
        fun_fact = await get_fun_fact(number)
        return {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": get_number_properties(number),
            "digit_sum": sum(map(int, str(abs(number)))),
            "fun_fact": fun_fact,
        }
    except (Exception, ValueError):
        return Response(content=json.dumps({"number": number, "error": True}), status_code=400, media_type="application/json")
        