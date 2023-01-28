from fastapi.routing import APIRouter

router = APIRouter(prefix='/utils',
                   tags=['Utils']
                   )


@router.api_route('', methods=['GET'])
def query():
    ...
