from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class UserRole(Enum):
    USER = "user"
    ADMIN = "admin"

@dataclass
class UserEntity:
    id: str
    name: str
    email: str
    role: UserRole = UserRole.USER
    created_at: datetime = datetime.now()
    last_login: datetime = datetime.now()
