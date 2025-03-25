from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from backend.utils.templates import templates

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    try:
        return templates.TemplateResponse("login.html", {"request": request})
    except Exception as e:
        return JSONResponse(content={"message": "FINBOT Login"})

@router.get("/dashboard.html", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@router.get("/stock.html", response_class=HTMLResponse)
async def read_stock(request: Request):
    return templates.TemplateResponse("stock.html", {"request": request})

@router.get("/chat.html", response_class=HTMLResponse)
async def read_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
