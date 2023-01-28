from datetime import datetime
from typing import Optional
from pydantic import BaseModel


from pydantic import BaseModel
from typing import List



class UpdateTagSchema(BaseModel):
    nome: Optional[str] 
    

class UpdateTransazioneSchema(BaseModel):
    date: Optional[str]
    costo: Optional[float]
    nome: Optional[str]
    descrizione: Optional[str]
    user_id: Optional[int]
    abbonamento_id: Optional[int]

class UpdateAbbonamentoSchema(BaseModel):
    giorno: Optional[int]
    mese: Optional[int]
    inizio: Optional[datetime]
    fine: Optional[datetime]
    costo: Optional[float]
    nome: Optional[str]
    descrizione: Optional[str]
    user_id: Optional[int]

class UpdateUserSchema(BaseModel):
    nome: Optional[str]
    cognome: Optional[str]
    nickname: Optional[str]
    email: Optional[str]
    password: Optional[str]