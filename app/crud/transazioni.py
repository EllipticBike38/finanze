from sqlalchemy.orm import Session
from models.models import Transazione
from .base import baseCRUD
import schemas


class transazioniCRUD(baseCRUD):
    obj_class=Transazione

transazioni=transazioniCRUD()