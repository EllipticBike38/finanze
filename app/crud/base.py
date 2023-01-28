from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Type
import schemas


class baseCRUD():
    obj_class:Type
    
    def create(self, db: Session, obj: Type[BaseModel]):
        obj = self.obj_class(**obj.dict(exclude_none=True))
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, id: int, obj: Type[BaseModel]):
        db.query(self.obj_class).filter(self.obj_class.id == id).update(
            obj.dict(exclude_none=True))
        db.commit()
        obj = db.get(self.obj_class, id)
        return obj

    def get(self, db: Session, id: int):
        obj = db.get(self.obj_class, id)
        return obj

    def get_all(self, db: Session):
        all=db.query(self.obj_class).all()
        return all

    def get_by_kwargs(self, db: Session, **kwargs):
        all=db.get(self.obj_class, kwargs)
        return all

    def delete(self, db: Session, id):
        obj = db.get(self.obj_class, id)
        db.delete(obj)
        db.commit()
        return id


