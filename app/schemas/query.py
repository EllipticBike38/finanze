from datetime import datetime
from typing import Optional


from pydantic import BaseModel, Field
from typing import List

class QueryTagSchema(BaseModel):
    id: int
    nome: str
    transactions: List[int] = Field([])

class QueryTransazioneSchema(BaseModel):
    id: int
    date: str
    costo: float
    nome: str
    descrizione: Optional[str]
    user_id: int
    abbonamento_id: Optional[int]
    tags: List[int] = Field([])

class QueryAbbonamentoSchema(BaseModel):
    id: int
    giorno: int
    mese: int
    inizio: datetime
    fine: Optional[datetime]
    costo: float
    nome: str
    descrizione: Optional[str]
    user_id: int
    transazioni: List[int] = Field([])

class QueryUserSchema(BaseModel):
    id: int
    nome: str
    cognome: str
    nickname: str
    email: str
    password: str
    transazioni: List[int] = Field([])
    abbonamenti: List[int] = Field([])

class QueryUserList(BaseModel):
    users:List[QueryUserSchema]