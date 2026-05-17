"""
Rotas do CRUD de Usuários
Guard.IA — Monitoramento Legislativo
"""
 
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
 
from database import get_db, engine
from models import Base, Usuario
from schemas import UsuarioCreate, UsuarioUpdate, UsuarioResponse
 
# Cria as tabelas no banco ao iniciar
Base.metadata.create_all(bind=engine)
 
app = FastAPI(
    title="Guard.IA — API de Usuários",
    description="CRUD de usuários para o sistema de monitoramento legislativo",
    version="1.0.0",
)
 
# Configuração de hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
 
 
def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)
 
 
def verificar_senha(senha: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha, senha_hash)
 
 
# ─────────────────────────────────────────────
# CREATE — Cadastrar usuário
# ─────────────────────────────────────────────
 
@app.post("/usuarios", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar_usuario(dados: UsuarioCreate, db: Session = Depends(get_db)):
    """Cria um novo usuário. O e-mail deve ser único."""
 
    # Verifica se e-mail já existe
    existente = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado."
        )
 
    novo = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha_hash=hash_senha(dados.senha),
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
 
 
# ─────────────────────────────────────────────
# READ — Buscar usuário por ID
# ─────────────────────────────────────────────
 
@app.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Retorna os dados de um usuário pelo ID."""
 
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado."
        )
    return usuario
 
 
# ─────────────────────────────────────────────
# READ — Listar todos os usuários
# ─────────────────────────────────────────────
 
@app.get("/usuarios", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    """Retorna a lista de todos os usuários cadastrados."""
    return db.query(Usuario).all()
 
 
# ─────────────────────────────────────────────
# UPDATE — Atualizar usuário
# ─────────────────────────────────────────────
 
@app.patch("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def atualizar_usuario(usuario_id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    """Atualiza nome, e-mail ou senha de um usuário. Todos os campos são opcionais."""
 
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado."
        )
 
    if dados.nome:
        usuario.nome = dados.nome
    if dados.email:
        usuario.email = dados.email
    if dados.senha:
        usuario.senha_hash = hash_senha(dados.senha)
 
    db.commit()
    db.refresh(usuario)
    return usuario
 
 
# ─────────────────────────────────────────────
# DELETE — Remover usuário
# ─────────────────────────────────────────────
 
@app.delete("/usuarios/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    """Remove um usuário pelo ID."""
 
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado."
        )
 
    db.delete(usuario)
    db.commit()
 
 
# ─────────────────────────────────────────────
# LOGIN — Verificar credenciais
# ─────────────────────────────────────────────
 
@app.post("/login")
def login(email: str, senha: str, db: Session = Depends(get_db)):
    """Verifica e-mail e senha. Retorna os dados do usuário se corretos."""
 
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario or not verificar_senha(senha, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha incorretos."
        )
 
    return {"mensagem": "Login realizado com sucesso.", "usuario_id": usuario.id}