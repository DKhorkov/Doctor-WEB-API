from typing import Dict
from werkzeug.security import generate_password_hash


ALLOWED_USERS: Dict = {
    'admin': generate_password_hash('admin'),
    'allowed_user': generate_password_hash('allowed_user')
}
