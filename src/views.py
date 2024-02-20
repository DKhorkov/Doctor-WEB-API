import os

from flask import request, Response, json, send_file
from typing import AnyStr, Optional, Type
from pathlib import Path
from werkzeug.datastructures import FileStorage

from .auth import login_required
from .configs import RESPONSE_CONTENT_TYPE, UPLOAD_DIR, FILE_PREFIX_LENGTH, ResponseMessageKeys, RequestKeys, \
    FileExtension
from .status_codes import StatusCodes
from .response_messages import ErrorMessages, SuccessMessages
from .hasher import Hasher
from .db import db, Users, Files, InvalidFileOwnerError


@login_required
def upload_view() -> Response:
    file: FileStorage = request.files.get(RequestKeys.file.value)
    if not file:
        return Response(
            response=json.dumps(ErrorMessages.no_file_key.value),
            status=StatusCodes.HTTP_422_UNPROCESSABLE_ENTITY.value,
            content_type=RESPONSE_CONTENT_TYPE
        )

    filename: AnyStr = file.filename
    file_extension: AnyStr = filename.split(FileExtension.separator.value)[FileExtension.index.value]

    # On case, if different users will upload file with the equal name:
    filename_for_hash: AnyStr = f'{filename}_{request.authorization.username}'
    
    hashed_filename: AnyStr = Hasher.hash(filename_for_hash)
    filename_prefix: AnyStr = hashed_filename[:FILE_PREFIX_LENGTH]
    file_folder_path: Path = UPLOAD_DIR / filename_prefix
    if not os.path.exists(file_folder_path):
        os.makedirs(file_folder_path, exist_ok=True)

    full_hashed_filename: AnyStr = f'{hashed_filename}{FileExtension.separator.value}{file_extension}'
    file.save(dst=file_folder_path / full_hashed_filename)

    user: Type[Users] = db.save_user(username=request.authorization.username)
    db.save_file(
        filename=filename,
        hashed_filename=hashed_filename,
        filename_prefix=filename_prefix,
        full_hashed_filename=full_hashed_filename,
        user=user
    )

    response_message: AnyStr = SuccessMessages.uploaded.value
    response_message[ResponseMessageKeys.file_hash.value] = hashed_filename
    return Response(
        response=json.dumps(response_message),
        status=StatusCodes.HTTP_201_CREATED.value,
        content_type=RESPONSE_CONTENT_TYPE
    )


def query_download_view() -> Response:
    hashed_filename: AnyStr = __get_hashed_filename_from_query()
    return __download_logic(hashed_filename=hashed_filename)


def param_download_view(hashed_filename: AnyStr) -> Response:
    return __download_logic(hashed_filename=hashed_filename)


def __download_logic(hashed_filename: Optional[AnyStr]) -> Response:
    if not hashed_filename:
        return __send_empty_hashed_filename_response()

    file: Type[Files] = db.select_file(hashed_filename=hashed_filename)
    if not file:
        return __send_file_not_found_response()

    return send_file(
        path_or_file=UPLOAD_DIR / file.filename_prefix / file.full_hashed_filename,
        as_attachment=True,
        download_name=file.filename
    )


@login_required
def query_delete_view() -> Response:
    hashed_filename: AnyStr = __get_hashed_filename_from_query()
    return __delete_logic(hashed_filename=hashed_filename)


@login_required
def param_delete_view(hashed_filename: AnyStr) -> Response:
    return __delete_logic(hashed_filename=hashed_filename)


def __delete_logic(hashed_filename: Optional[AnyStr]) -> Response:
    if not hashed_filename:
        return __send_empty_hashed_filename_response()

    file: Type[Files] = db.select_file(hashed_filename=hashed_filename)
    if not file:
        return __send_file_not_found_response()

    try:
        user: Type[Users] = db.save_user(username=request.authorization.username)
        db.delete_file(hashed_filename=hashed_filename, user=user)
        os.remove(UPLOAD_DIR / file.filename_prefix / file.full_hashed_filename)
    except InvalidFileOwnerError as e:
        return Response(
            response=json.dumps(str(e)),
            status=StatusCodes.HTTP_200_OK.value,
            content_type=RESPONSE_CONTENT_TYPE
        )

    response_message: AnyStr = SuccessMessages.deleted.value
    response_message[ResponseMessageKeys.detail.value] += hashed_filename
    return Response(
        response=json.dumps(response_message),
        status=StatusCodes.HTTP_200_OK.value,
        content_type=RESPONSE_CONTENT_TYPE
    )


def __get_hashed_filename_from_query() -> Optional[AnyStr]:
    return request.args.get(RequestKeys.hashed_filename.value, request.args.get(''))


def __send_empty_hashed_filename_response() -> Response:
    return Response(
        response=json.dumps(ErrorMessages.no_hash_provided.value),
        status=StatusCodes.HTTP_422_UNPROCESSABLE_ENTITY.value,
        content_type=RESPONSE_CONTENT_TYPE
    )


def __send_file_not_found_response() -> Response:
    return Response(
        response=json.dumps(ErrorMessages.not_found.value),
        status=StatusCodes.HTTP_404_NOT_FOUND.value,
        content_type=RESPONSE_CONTENT_TYPE
    )
