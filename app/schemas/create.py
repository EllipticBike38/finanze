from datetime import datetime
from typing import Optional
from pydantic import BaseModel


from pydantic import BaseModel
from typing import List



class CreateTagSchema(BaseModel):
    nome: str 
    

class CreateTransazioneSchema(BaseModel):
    date: str
    costo: float
    nome: str
    descrizione: Optional[str]
    user_id: int
    abbonamento_id: Optional[int]

class CreateAbbonamentoSchema(BaseModel):
    giorno: int
    mese: int
    inizio: datetime
    fine: Optional[datetime]
    costo: float
    nome: str
    descrizione: Optional[str]
    user_id: int

class CreateUserSchema(BaseModel):
    nome: str
    cognome: str
    nickname: str
    email: str
    password: str