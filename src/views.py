import os

from flask import render_template, request, Response, json
from typing import AnyStr
from pathlib import Path
from werkzeug.datastructures import FileStorage

from .auth import login_required
from .configs import Templates, RESPONSE_CONTENT_TYPE, UPLOAD_DIR, FILE_PREFIX_LENGTH, ResponseMessageKeys, \
    RequestKeys, FileExtension
from .status_codes import StatusCodes
from .response_messages import ErrorMessages, SuccessMessages
from .hasher import Hasher


def homepage_view() -> AnyStr:
    return render_template(Templates.homepage.value)


@login_required
def upload_view() -> Response:
    file: FileStorage = request.files.get(RequestKeys.file.value)
    if not file:
        return Response(
            response=json.dumps(ErrorMessages.unprocessable_entity.value),
            status=StatusCodes.HTTP_422_UNPROCESSABLE_ENTITY.value,
            content_type=RESPONSE_CONTENT_TYPE
        )

    username: AnyStr = request.authorization.username

    filename: AnyStr = file.filename
    file_extension: AnyStr = filename.split(FileExtension.separator.value)[FileExtension.index.value]
    hashed_filename: AnyStr = Hasher.hash(filename)
    file_prefix: AnyStr = hashed_filename[:FILE_PREFIX_LENGTH]
    file_folder_path: Path = UPLOAD_DIR / file_prefix
    if not os.path.exists(file_folder_path):
        os.makedirs(file_folder_path, exist_ok=True)

    full_hashed_filename: AnyStr = f'{hashed_filename}{FileExtension.separator.value}{file_extension}'
    file.save(dst=file_folder_path / full_hashed_filename)

    response_message: AnyStr = SuccessMessages.uploaded.value
    response_message[ResponseMessageKeys.file_hash.value] = hashed_filename
    return Response(
        response=json.dumps(response_message),
        status=StatusCodes.HTTP_201_CREATED.value,
        content_type=RESPONSE_CONTENT_TYPE
    )
