from pydantic import BaseModel

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    status: bool
    usuario_nome: str 

class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    titulo: str
    descricao: str
    status: bool

class TarefaResponse(TarefaBase):
    id: int

    class Config:
        orm_mode = True
