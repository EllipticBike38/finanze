from fastapi import Body, Depends, Request
from fastapi.routing import APIRouter
from pydantic import Field
import schemas
from models.models import User
from crud import users
from dependencies import get_db
from errors import ConflictError, NotFoundError, response
router = APIRouter(prefix='/user',
                   tags=['Utenti']
                   )


@router.api_route('', methods=['GET'], response_model=schemas.QueryUserList )
def query(request: Request,
          db=Depends(get_db)):
    params = request.query_params._dict
    q_users = users.get_all(db)
    
    return {'users':[schemas.QueryUserSchema(**q_user.__dict__) for q_user in q_users]}


@router.api_route('', methods=['POST'], response_model=schemas.QueryUserSchema, responses=response([409]))
def create(
    user: schemas.CreateUserSchema,
    db=Depends(get_db)
):
    if any(tuple(u.email==user.email or u.nickname == user.nickname for u in users.get_all(db))):
        raise ConflictError
    user = users.create(db=db, obj=user)
    return user.__dict__


@router.api_route('', methods=['PUT'], response_model=schemas.QueryUserSchema, responses=response([404]))
def update(
    user: schemas.UpdateUserSchema,
    id:int,
    db=Depends(get_db)
):
    user = users.get(db, id)
    if not user:raise NotFoundError 
    user = users.update(db=db, id = id,obj=user)
    return user.__dict__


@router.api_route('', methods=['DELETE'], responses=response([404]))
def delete(
        user_id: int,
        db=Depends(get_db)):

    user = users.get(db, user_id)
    if not user:raise NotFoundError 
    final_id=users.delete(db, user_id)
    return {'id':final_id}
    ...


@router.api_route('/{user_id}', methods=['GET'], response_model=schemas.QueryUserSchema, responses=response([404]))
def get(
        user_id: int,
        db=Depends(get_db)):

    user = users.get(db, user_id)
    if not user:raise NotFoundError 
    return user.__dict__
