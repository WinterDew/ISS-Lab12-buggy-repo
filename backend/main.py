from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routes.items import router as items_router
from routes.analytics import router as analytics_router
from routes.quiz import router as quiz_router
from fastapi.staticfiles import StaticFiles
from routes.users import router as users_router
from fastapi.responses import FileResponse
import os
app = FastAPI()

app.include_router(items_router, prefix="/items")
app.include_router(analytics_router)
app.include_router(quiz_router)
app.include_router(users_router)

# Set up templates directory
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("../frontend", "index.html"))