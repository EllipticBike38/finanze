from fastapi import Body, Depends, Request
from fastapi.routing import APIRouter
from pydantic import Field
import schemas
from models.models import Abbonamento
from crud import abbonamenti
from dependencies import get_db

router = APIRouter(prefix='/subs',
                   tags=['Abbonamenti']
                   )


@router.api_route('', methods=['GET'], response_model=schemas.QueryAbbonamentoList)
def query(request: Request,
          db=Depends(get_db)):
    params = request.query_params._dict
    q_abbonamenti = abbonamenti.get_all(db)

    return {'abbonamenti': [schemas.QueryAbbonamentoSchema(**q_abbonamento.__dict__) for q_abbonamento in q_abbonamenti]}


@router.api_route('/user', methods=['GET'], response_model=schemas.QueryAbbonamentoList)
def query_by_user(request: Request,
                  user: int,
                  db=Depends(get_db)):

    q_abbonamenti = [abb for abb in abbonamenti.get_all(
        db) if abb.user_id == user]

    return {'abbonamenti': [schemas.QueryAbbonamentoSchema(**q_abbonamento.__dict__) for q_abbonamento in q_abbonamenti]}


@router.api_route('', methods=['POST'], response_model=schemas.QueryAbbonamentoSchema)
def create(
    abbonamento: schemas.CreateAbbonamentoSchema,
    db=Depends(get_db)
):
    abbonamento = abbonamenti.create(db=db, obj=abbonamento)
    return abbonamento.__dict__


@router.api_route('', methods=['PUT'], response_model=schemas.QueryAbbonamentoSchema)
def update(
    abbonamento: schemas.UpdateAbbonamentoSchema,
    id: int,
    db=Depends(get_db)
):
    abbonamento = abbonamenti.update(db=db, id=id, obj=abbonamento)
    return abbonamento.__dict__


@router.api_route('', methods=['DELETE'])
def delete(
        abbonamento_id: int,
        db=Depends(get_db)):
    final_id = abbonamenti.delete(db, abbonamento_id)
    return {'id': final_id}
    ...


@router.api_route('/{abbonamento_id}', methods=['GET'], response_model=schemas.QueryAbbonamentoSchema)
def get(
        abbonamento_id: int,
        db=Depends(get_db)):

    abbonamento = abbonamenti.get(db, abbonamento_id)
    return abbonamento.__dict__
