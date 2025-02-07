from fastapi import FastAPI
from controllers.usuarios_controller import router as usuario_router
from controllers.tarefa_controller import router as tarefa_router
from controllers.web_controller import router as web_router  # Importe o web_controller
from models.usuarios import Base as UsuarioBase
from models.tarefa import Base as TarefaBase
from database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Criar as tabelas no banco de dados
UsuarioBase.metadata.create_all(bind=engine)
TarefaBase.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar Jinja2 e arquivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Registrar os routers
app.include_router(usuario_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(tarefa_router, prefix="/tarefas", tags=["Tarefas"])
app.include_router(web_router, tags=["Web"])  # Registrar o novo router para a interface web
