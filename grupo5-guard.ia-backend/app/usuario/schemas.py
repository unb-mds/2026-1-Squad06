
#Schemas de Usuário (validação de entrada e saída)

from pydantic import BaseModel, EmailStr
from datetime import datetime


# ── Criação de usuário (o que o front manda) ──
class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str


# ── Atualização de usuário (campos opcionais) ──
class UsuarioUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    senha: str | None = None


# ── Resposta da API (o que o front recebe — sem senha) ──
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    ativo: bool
    criado_em: datetime

    class Config:
        from_attributes = True