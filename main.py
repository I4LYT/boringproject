# --------------------------------------------------------------------------
# ---------- Copyright(c) 2025, L1FE/I4LYT. All rights reserved. -----------
# --------------------------------------------------------------------------
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import settings

app = FastAPI()

# Mount static files for CSS and JavaScript
app.mount("/static", StaticFiles(directory="static"), name="static")
# Mount templates for HTML rendering
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/apps") # All the "apps"
def games(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.port)  # Change the port in settings.py