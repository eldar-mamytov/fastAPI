from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import os
import random

app = FastAPI()

# Get the absolute path of the frontend directory
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))

# Ensure FastAPI can find the frontend directory
if not os.path.exists(frontend_path):
    raise RuntimeError(f"Directory '{frontend_path}' does not exist")

app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(frontend_path, "index.html"))

# Greeting endpoint with multiple messages
greetings = ["Hello from FastAPI!", "Hey there!", "Hi! How's it going?", "Greetings!"]

@app.get("/greet")
async def greet():
    greeting = random.choice(greetings)
    return JSONResponse(content = {"message": greeting})

# Random fact endpoint with multiple facts
facts = [
    "The Eiffel Tower can be 15 cm taller during hot days.",
    "Bananas are berries, but strawberries aren't.",
    "Honey never spoils.",
    "Octopuses have three hearts."
]

@app.get("/random-fact")
async def random_fact():
    fact = random.choice(facts)
    return JSONResponse(content = {"fact": fact})

# Calculator endpoint
# Calculator Endpoint
@app.get("/calculate")
async def calculate(num1: float, num2: float, operation: str):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return JSONResponse(content={"error": "Invalid operation"}, status_code=400)
    
    return JSONResponse(content={"result": result})

# Reverse Text Endpoint
@app.get("/reverse-text")
async def reverse_text(text: str):
    return JSONResponse(content={"reversed": text[::-1]})

# Word Count Endpoint
@app.get("/word-count")
async def word_count(text: str):
    words = text.split()
    return JSONResponse(content={"word_count": len(words)})
