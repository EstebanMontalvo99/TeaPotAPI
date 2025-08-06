from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resto de endpoints
@app.get("/status")
def get_status():
    return {"damaged_system": "engine"}

@app.get("/repair-bay", response_class=HTMLResponse)
def get_repair_bay():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">ENG-04</div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/teapot", status_code=418, responses={418: {"description": "I'm a teapot"}})
def post_teapot():
    return JSONResponse(
        status_code=418,
        content={"detail": "I'm a teapot "}
    )
