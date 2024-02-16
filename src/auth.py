from functools import wraps
from flask import request, Response, json
from typing import AnyStr, Callable, Any, Dict, Union
from werkzeug.security import check_password_hash
from werkzeug.datastructures import Authorization

from .status_codes import StatusCodes
from .configs import RESPONSE_CONTENT_TYPE
from .users import ALLOWED_USERS
from .response_messages import ErrorMessages


def login_required(route: Callable) -> Callable:

    @wraps(route)
    def wrapped_view(**kwargs: Dict[Any, Any]) -> Union[Callable | Response]:
        auth: Authorization = request.authorization
        if not (auth and __check_auth(auth.username, auth.password)):
            return Response(
                response=json.dumps(ErrorMessages.unauthorized.value),
                status=StatusCodes.HTTP_401_UNAUTHORIZED.value,
                content_type=RESPONSE_CONTENT_TYPE
            )

        return route(**kwargs)

    return wrapped_view


def __check_auth(username: AnyStr, password: AnyStr) -> bool:
    if username and username in ALLOWED_USERS and check_password_hash(ALLOWED_USERS[username], password):
        return True
    else:
        return False
