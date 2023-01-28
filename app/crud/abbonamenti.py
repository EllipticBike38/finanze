from sqlalchemy.orm import Session
from models.models import Abbonamento
from .base import baseCRUD
import schemas


class abbonamentiCRUD(baseCRUD):
    obj_class=Abbonamento

abbonamenti=abbonamentiCRUD()