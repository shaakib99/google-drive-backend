from abc import ABC, abstractmethod
from common.models.dependencies import CommonDependencies

class GuardABC(ABC):
    def __init__(self, ):
        pass

    @abstractmethod
    def dispatch(self, dependencies: CommonDependencies) -> tuple:
        pass