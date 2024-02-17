from enum import Enum


class StatusCodes(Enum):
    # Successful responses:
    HTTP_200_OK: int = 200
    HTTP_201_CREATED: int = 201

    # Client error responses:
    HTTP_401_UNAUTHORIZED: int = 401
    HTTP_404_NOT_FOUND: int = 404
    HTTP_405_METHOD_NOT_ALLOWED: int = 405
    HTTP_422_UNPROCESSABLE_ENTITY: int = 422
