from typing import AnyStr
from enum import Enum
from pathlib import Path


class Templates(Enum):
    homepage: AnyStr = 'homepage.html'


class Methods(Enum):
    get: AnyStr = 'GET'
    post: AnyStr = 'POST'
    put: AnyStr = 'PUT'
    delete: AnyStr = 'DELETE'
    patch: AnyStr = 'PATCH'
    options: AnyStr = 'OPTIONS'


class URLRules(Enum):
    homepage: AnyStr = '/'
    upload: AnyStr = '/upload'


class URLNames(Enum):
    homepage: AnyStr = 'Homepage'
    upload: AnyStr = 'Upload'


class RequestKeys(Enum):
    file: AnyStr = 'file'


class ResponseMessageKeys(Enum):
    detail: AnyStr = 'detail'
    file_hash: AnyStr = 'file_hash'


class FileExtension(Enum):
    separator: AnyStr = '.'
    index: int = -1


UPLOAD_DIR: Path = Path('./store/')

FILE_PREFIX_LENGTH: int = 2

RESPONSE_CONTENT_TYPE: AnyStr = 'application/json'

ENCODING: AnyStr = 'utf-8'
