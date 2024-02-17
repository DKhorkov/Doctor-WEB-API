from enum import Enum
from typing import AnyStr, Dict

from .configs import ResponseMessageKeys, PROJECT_DOCUMENTATION_URL


class ErrorMessages(Enum):
    unauthorized: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'You are not authorized or not in allowed users. '
                                               'In first case, use Basic-authorization to use this route.'
    }

    no_file_key: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'No "file" key was provided.'
                                               'To send file use "file" key and body format should be "form-data".'
    }

    method_not_allowed: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'Method you are using is not allowed for this route.'
    }

    not_found: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'File with provided hash is not found!.'
    }

    no_hash_provided: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': f'Hash for file was not provided correctly. To use this route, '
                                               f'please, send hash in request to this route according '
                                               f'<a href="{PROJECT_DOCUMENTATION_URL}">Documentation</a>.'
    }


class SuccessMessages(Enum):
    uploaded: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'Successfully uploaded file.',
        f'{ResponseMessageKeys.file_hash.value}': ''  # will be updated dynamically
    }

    deleted: Dict[AnyStr, AnyStr] = {
        # will be updated dynamically:
        f'{ResponseMessageKeys.detail.value}': 'Successfully deleted file for provided hash='
    }
