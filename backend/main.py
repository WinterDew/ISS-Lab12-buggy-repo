from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router)
app.include_router(quiz_router)

# Set up templates directory
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

# @app.get("/home", response_class=HTMLResponse)
# async def get_home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
