from fastapi.routing import APIRouter
from errors.errors import errors

router = APIRouter(prefix='/utils',
                   tags=['Utils']
                   )


@router.api_route('', methods=['GET'])
def test_errors(error:int):
    raise errors[error]
