from abc import ABC, abstractmethod
from fastapi import Request, Response

class GuardABC(ABC):
    def __init__(self, ):
        pass

    @abstractmethod
    def invoke_guard(self, req: Request, res: Response):
        pass