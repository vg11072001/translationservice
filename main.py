from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import router as api_router
from app.database import init_db
from app.services import log_translation


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static/templates")


@app.get("/", response_class=HTMLResponse)
async def serve_homepage(request: Request):
    log_translation(
        original_text=None,
        target_language=None,
        translated_text=None,
        request_type="GET",
        endpoint="/",
    )
    return templates.TemplateResponse("index.html", {"request": request})


@app.on_event("startup")
async def startup_event():
    init_db()


app.include_router(api_router, prefix="/api", tags=["translation"])


@app.get("/health")
def health_check():
    log_translation(
        original_text=None,
        target_language=None,
        translated_text=None,
        request_type="GET",
        endpoint="/health",
    )
    return {"status": "OK"}
