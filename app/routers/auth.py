from fastapi.routing import APIRouter

router = APIRouter(prefix='/auth',
                   tags=['Autenticazione']
                   )


@router.api_route('', methods=['POST'])
def login():
    ...


@router.api_route('', methods=['DELETE'])
def logout():
    ...
