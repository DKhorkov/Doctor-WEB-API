import os
from typing import AnyStr
from enum import Enum
from pathlib import Path


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
    query_download: AnyStr = '/download'
    param_download: AnyStr = '/download/<string:hashed_filename>'
    query_delete: AnyStr = '/delete'
    param_delete: AnyStr = '/delete/<string:hashed_filename>'


class URLNames(Enum):
    upload: AnyStr = 'Upload'
    query_download: AnyStr = 'Query download'
    param_download: AnyStr = 'Parametrized download'
    query_delete: AnyStr = 'Query delete'
    param_delete: AnyStr = 'Parametrized delete'


class RequestKeys(Enum):
    file: AnyStr = 'file'
    hashed_filename: AnyStr = 'hashed_filename'


class ResponseMessageKeys(Enum):
    detail: AnyStr = 'detail'
    file_hash: AnyStr = 'file_hash'


class FileExtension(Enum):
    separator: AnyStr = '.'
    index: int = -1


UPLOAD_DIR: Path = Path(f'{os.getcwd()}/store/')

FILE_PREFIX_LENGTH: int = 2

RESPONSE_CONTENT_TYPE: AnyStr = 'application/json'

ENCODING: AnyStr = 'utf-8'

__DATABASE_FOLDER: Path = Path(f'{os.getcwd()}/database/')
if not __DATABASE_FOLDER.exists():
    os.makedirs(__DATABASE_FOLDER)

DATABASE_URL: AnyStr = f'sqlite:///{__DATABASE_FOLDER}/db.sqlite'

PROJECT_DOCUMENTATION_URL: AnyStr = 'https://github.com/DKhorkov/Doctor-WEB-API'
