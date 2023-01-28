from fastapi import Body, Depends, Request
from fastapi.routing import APIRouter
from pydantic import Field
import schemas
from models.models import User
from crud import users
from dependencies import get_db
router = APIRouter(prefix='/user',
                   tags=['Utenti']
                   )


@router.api_route('', methods=['GET'], response_model=schemas.QueryUserList )
def query(request: Request,
          db=Depends(get_db)):
    params = request.query_params._dict
    q_users = users.get_all(db)
    
    return {'users':[schemas.QueryUserSchema(**q_user.__dict__) for q_user in q_users]}


@router.api_route('', methods=['POST'], response_model=schemas.QueryUserSchema)
def create(
    user: schemas.CreateUserSchema,
    db=Depends(get_db)
):
    user = users.create(db=db, obj=user)
    return user.__dict__


@router.api_route('', methods=['PUT'], response_model=schemas.QueryUserSchema)
def update(
    user: schemas.UpdateUserSchema,
    id:int,
    db=Depends(get_db)
):
    user = users.update(db=db, id = id,obj=user)
    return user.__dict__


@router.api_route('', methods=['DELETE'])
def delete(
        user_id: int,
        db=Depends(get_db)):
    final_id=users.delete(db, user_id)
    return {'id':final_id}
    ...


@router.api_route('/{user_id}', methods=['GET'], response_model=schemas.QueryUserSchema)
def get(
        user_id: int,
        db=Depends(get_db)):

    user = users.get(db, user_id)
    return user.__dict__
