from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import home, stock, chat
from utils.logger import setup_logger
import os

app = FastAPI()
logger = setup_logger()

# Mount static files if available
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "..", "frontend", "static")

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include routers
app.include_router(home.router)
app.include_router(stock.router)
app.include_router(chat.router)

# Health check route (Avoids conflict with home.router)
@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))  # ✅ Ensure Cloud Run uses PORT=8080
    uvicorn.run(app, host="0.0.0.0", port=port)


