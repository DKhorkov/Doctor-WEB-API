from hashlib import sha256
from typing import AnyStr

from .configs import ENCODING


class Hasher:

    __hash_algorithm = sha256()

    @classmethod
    def __reload(cls) -> None:
        """
        Reloading hash algorithm every usage due to update() method logic.
        """
        cls.__hash_algorithm = sha256()

    @classmethod
    def hash(cls, data: AnyStr) -> AnyStr:
        cls.__hash_algorithm.update(data.encode(ENCODING))
        hashed_value: AnyStr = cls.__hash_algorithm.hexdigest()
        cls.__reload()
        return hashed_value
