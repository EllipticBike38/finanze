from fastapi.routing import APIRouter

router = APIRouter(prefix='/subs',
                   tags=['Abbonamenti']
                   )


@router.api_route('', methods=['GET'])
def query():
    ...


@router.api_route('', methods=['POST'])
def create():
    ...


@router.api_route('', methods=['PUT'])
def update():
    ...


@router.api_route('', methods=['DELETE'])
def delete():
    ...
