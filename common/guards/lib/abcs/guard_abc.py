from abc import ABC, abstractmethod
from common.models.dependencies_model import CommonDependenciesModel

class GuardABC(ABC):
    def __init__(self, ):
        pass

    @abstractmethod
    def dispatch(self, dependencies: CommonDependenciesModel):
        pass