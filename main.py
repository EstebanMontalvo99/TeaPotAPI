from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Diccionario de códigos
system_codes = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Variable global para almacenar el sistema dañado
damaged_system = random.choice(list(system_codes.keys()))

@app.get("/status")
def get_status():
    return {"damaged_system": damaged_system}

@app.get("/repair-bay", response_class=HTMLResponse)
def get_repair_bay():
    code = system_codes.get(damaged_system, "UNKNOWN")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{code}</div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/teapot", status_code=418, responses={418: {"description": "I'm a teapot"}})
def post_teapot():
    return JSONResponse(
        status_code=418,
        content={"detail": "I'm a teapot"}
    )
