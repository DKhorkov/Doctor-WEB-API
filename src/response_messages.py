from enum import Enum
from typing import AnyStr, Dict

from .configs import ResponseMessageKeys


class ErrorMessages(Enum):
    unauthorized: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'You are not authorized or not in allowed users. '
                                               'In first case, use Basic-authorization to use this route.'
    }

    unprocessable_entity: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'No file key was provided of file format is invalid. '
                                               'To send file use "file" key and body format should be "form-data".'
    }

    method_not_allowed: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'Method you are using is not allowed for this route.'
    }


class SuccessMessages(Enum):
    uploaded: Dict[AnyStr, AnyStr] = {
        f'{ResponseMessageKeys.detail.value}': 'Successfully uploaded file.',
        f'{ResponseMessageKeys.file_hash.value}': ''  # will be updated dynamically
    }
