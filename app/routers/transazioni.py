from fastapi import Body, Depends, Request
from fastapi.routing import APIRouter
from pydantic import Field
import schemas
from models.models import Transazione
from crud import transazioni, users, abbonamenti
from dependencies import get_db

router = APIRouter(prefix='/transaction',
                   tags=['Transazioni']
                   )


@router.api_route('', methods=['GET'], response_model=schemas.QueryTransazioneList)
def query(request: Request,
          db=Depends(get_db)):
    params = request.query_params._dict
    q_transazioni = transazioni.get_all(db)

    return {'transazioni': [schemas.QueryTransazioneSchema(**q_transazione.__dict__) for q_transazione in q_transazioni]}


@router.api_route('/user', methods=['GET'], response_model=schemas.QueryTransazioneList)
def query_by_user(request: Request,
                  user: int,
                  db=Depends(get_db)):

    q_transazioni = users.get(db, user).transazioni

    return {'transazioni': [schemas.QueryTransazioneSchema(**q_transazione.__dict__) for q_transazione in q_transazioni]}


@router.api_route('/abbonamento', methods=['GET'], response_model=schemas.QueryTransazioneList)
def query_by_abbonamenti(request: Request,
                         abbonamento: int,
                         db=Depends(get_db)):

    q_transazioni = abbonamenti.get(db, abbonamento).transazioni

    return {'transazioni': [schemas.QueryTransazioneSchema(**q_transazione.__dict__) for q_transazione in q_transazioni]}


@router.api_route('', methods=['POST'], response_model=schemas.QueryTransazioneSchema)
def create(
    transazione: schemas.CreateTransazioneSchema,
    db=Depends(get_db)
):
    transazione = transazioni.create(db=db, obj=transazione)
    return transazione.__dict__


@router.api_route('', methods=['PUT'], response_model=schemas.QueryTransazioneSchema)
def update(
    transazione: schemas.UpdateTransazioneSchema,
    id: int,
    db=Depends(get_db)
):
    transazione = transazioni.update(db=db, id=id, obj=transazione)
    return transazione.__dict__


@router.api_route('', methods=['DELETE'])
def delete(
        transazione_id: int,
        db=Depends(get_db)):
    final_id = transazioni.delete(db, transazione_id)
    return {'id': final_id}
    ...


@router.api_route('/{transazione_id}', methods=['GET'], response_model=schemas.QueryTransazioneSchema)
def get(
        transazione_id: int,
        db=Depends(get_db)):

    transazione = transazioni.get(db, transazione_id)
    return transazione.__dict__
