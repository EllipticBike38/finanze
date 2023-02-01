from fastapi.exceptions import RequestValidationError
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse


async def foreign_key_exception_handler(request, exc: IntegrityError):
    return JSONResponse(status_code=404, content={"error": str(exc)})


async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"error": str(exc)})


class GenericError(Exception):
    code = 400
    msg = 'Generic Exception'

    def __init__(self, code=None, msg=None, *args) -> None:
        super().__init__(*args)
        if code:
            self.code = code
        if msg:
            self.msg = msg

    def __str__(self) -> str:
        return self.msg


async def generic_error_handler(request, exc: GenericError):
    return JSONResponse(status_code=400, content={"error": exc.__str__()})


class UnauthorizedError(GenericError):
    code = 401
    msg = "Unauthorized"

    def __init__(self, message=None, *args) -> None:
        super().__init__(*args)
        if message:
            self.msg = message


class ForbiddenError(GenericError):
    code = 403
    msg = "Forbidden"

    def __init__(self, message=None, *args) -> None:
        super().__init__(*args)
        if message:
            self.msg = message


class NotFoundError(GenericError):
    code = 404
    msg = "Not Found"

    def __init__(self, message=None, *args) -> None:
        super().__init__(*args)
        if message:
            self.msg = message + ' Not Found'


class MethodNotAllowedError(GenericError):
    code = 405
    msg = "Method Not Allowed"

    def __init__(self, message=None, *args) -> None:
        super().__init__(*args)
        if message:
            self.msg = message


class NotAcceptableError(GenericError):
    code = 406
    msg = "Not Acceptable"

    def __init__(self, message=None, *args) -> None:
        super().__init__(*args)
        if message:
            self.msg = message


class ConflictError(GenericError):
    code = 409
    msg = "Conflict"

    def __init__(self, message=None, *args) -> None:
        super().__init__(*args)
        if message:
            self.msg = message + ' Already Exixsts'


async def not_found_error_handler(request, exc: NotFoundError):
    return JSONResponse(status_code=exc.code, content={"error": exc.msg})


async def unauthorized_error_handler(request, exc: UnauthorizedError):
    return JSONResponse(status_code=exc.code, content={"error": exc.msg})


async def forbidden_error_handler(request, exc: ForbiddenError):
    return JSONResponse(status_code=exc.code, content={"error": exc.msg})


async def method_not_allowed_error_handler(request, exc: MethodNotAllowedError):
    return JSONResponse(status_code=exc.code, content={"error": exc.msg})


async def not_acceptable_error_handler(request, exc: NotAcceptableError):
    return JSONResponse(status_code=exc.code, content={"error": exc.msg})


async def conflict_error_handler(request, exc: ConflictError):
    return JSONResponse(status_code=exc.code, content={"error": exc.msg})

handlers = (foreign_key_exception_handler,
            validation_exception_handler,
            generic_error_handler,
            not_found_error_handler,
            unauthorized_error_handler,
            forbidden_error_handler,
            method_not_allowed_error_handler,
            not_acceptable_error_handler,
            conflict_error_handler)

errors = (
    IntegrityError,
    RequestValidationError,
    GenericError,
    NotFoundError,
    UnauthorizedError,
    ForbiddenError,
    MethodNotAllowedError,
    NotAcceptableError,
    ConflictError
    )

responses={
    #GenericError
    400 : {
        'details' : GenericError.msg,
        "content": {
                "application/json": {
                    "example": {"error":GenericError.msg}
                }
            },
    } ,
    #UnauthorizedError
    401 : {
        'details' : UnauthorizedError.msg,
        "content": {
                "application/json": {
                    "example": {"error":UnauthorizedError.msg}
                }
            },
    } ,
    #ForbiddenError
    403 : {
        'details' : ForbiddenError.msg,
        "content": {
                "application/json": {
                    "example": {"error":ForbiddenError.msg}
                }
            },
    } ,
    #NotFoundError
    404 : {
        'details' : NotFoundError.msg,
        "content": {
                "application/json": {
                    "example": {"error": "user Not Found"}
                }
            },
    } ,
    #MethodNotAllowedError
    405 : {
        'details' : MethodNotAllowedError.msg,
        "content": {
                "application/json": {
                    "example": {"error":MethodNotAllowedError.msg}
                }
            },
    } ,
    #NotAcceptableError
    406 : {
        'details' : NotAcceptableError.msg,
        "content": {
                "application/json": {
                    "example": {"error":NotAcceptableError.msg}
                }
            },
    } ,
    #ConflictError
    409 : {
        'details' : ConflictError.msg,
        "content": {
                "application/json": {
                    "example": {"error":ConflictError.msg}
                }
            },
    } ,
}

def response(codes:list[int]):
    a=dict()
    for code in codes:
        if code in responses.keys():
            a[code]= responses.get(code)
    return a