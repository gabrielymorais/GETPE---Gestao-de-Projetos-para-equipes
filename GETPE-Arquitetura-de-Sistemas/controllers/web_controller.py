from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from services.tarefa_service import obter_tarefas

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def listar_registros(request: Request, db: Session = Depends(get_db)):
    tarefas = obter_tarefas(db)  # Obter tarefas do banco
    return templates.TemplateResponse("index.html", {"request": request, "tarefas": tarefas})

@router.get("/form/", response_class=HTMLResponse)
async def exibir_formulario(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
