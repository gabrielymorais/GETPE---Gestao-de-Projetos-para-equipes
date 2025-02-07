from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.tarefa_service import (
    adicionar_tarefa,
    obter_tarefas,
    atualizar_tarefa,
    remover_tarefa,
)
from schemas.tarefa import TarefaCreate, TarefaResponse, TarefaUpdate

router = APIRouter()

@router.post("/criar-tarefa/", response_model=TarefaResponse)
def criar_tarefa_endpoint(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    try:
        return adicionar_tarefa(
            db=db,
            titulo=tarefa.titulo,
            descricao=tarefa.descricao,
            status=tarefa.status,
            usuario_nome=tarefa.usuario_nome,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/listar-tarefas/", response_model=list[TarefaResponse])
def listar_tarefas_endpoint(db: Session = Depends(get_db)):
    return obter_tarefas(db=db)

@router.put("/editar-tarefa/{id}", response_model=TarefaResponse)
def editar_tarefa_endpoint(id: int, tarefa: TarefaUpdate, db: Session = Depends(get_db)):
    try:
        return atualizar_tarefa(db=db, tarefa_id=id, tarefa_atualizada=tarefa)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/deletar-tarefa/{id}")
def deletar_tarefa_endpoint(id: int, db: Session = Depends(get_db)):
    sucesso = remover_tarefa(db=db, tarefa_id=id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"detail": "Tarefa excluída com sucesso"}
