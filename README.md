# fastAPI project

This is simple fastAPI project with a backend built using python and frontend using HTML, CSS, JavaScript.
It has multiple endpoints which do different type of task.

# Endpoints

1) Root endpoint "/" - serves the frontend index.html
2) Greeting endpoint "/greet" - returns a greeting message
3) Random fact endpoint "/random-fact" - returns a random fact
4) Calculator endpoint "/calculate" - does calculating operations
5) Reverse endpoint "/reverse-text" - reverses user's input text
6) Word count endpoint "/word-count" - counts words in user's text

# Installation

1) Clone my repository:
    git clone git@github.com:eldar-mamytov/fastAPI.git

2) Create and activate a virtual environment:
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate

3) Install all depencencies:
    pip install -r requirements.txt 

# Virtual Environemnt Run

1) Run virtual environment:
    cd backend
    uvicorn main:app --reload

2) Open browser:
    127.0.0.1:8000 or localhost:8000 


