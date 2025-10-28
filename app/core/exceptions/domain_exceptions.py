 
class DomainError(Exception):
    """Base exception for domain errors."""
    pass

class NotFoundError(DomainError):
    """Raised when an entity is not found."""
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message)
