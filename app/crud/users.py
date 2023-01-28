from sqlalchemy.orm import Session
from models.models import User
from .base import baseCRUD
import schemas


class userCRUD(baseCRUD):
    obj_class=User


users = userCRUD()
