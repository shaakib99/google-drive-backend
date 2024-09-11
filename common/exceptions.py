from typing import Any, Dict
from fastapi import HTTPException

class NotFoundException(HTTPException):
    def __init__(self, message: str = 'Resource Not Found'):
        super().__init__(status_code = 404, detail = message)

class UnauthorizeException(HTTPException):
    def __init__(self, message: str = 'Not authorize'):
        super().__init__(status_code = 401, detail = message)
    
class BadRequestException(HTTPException):
    def __init__(self, message: str = 'Bad Request'):
        super().__init__(status_code = 400, detail = message)

class TooManyRequestException(HTTPException):
    def __init__(self, message: str = 'Too many request') -> None:
        super().__init__(status_code = 429, detail = message)