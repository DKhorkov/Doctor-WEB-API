from enum import Enum


class StatusCodes(Enum):
    # Successful responses:
    HTTP_201_CREATED: int = 201

    # Client error responses:
    HTTP_401_UNAUTHORIZED: int = 401
    HTTP_422_UNPROCESSABLE_ENTITY: int = 422
    HTTP_405_METHOD_NOT_ALLOWED: int = 405

