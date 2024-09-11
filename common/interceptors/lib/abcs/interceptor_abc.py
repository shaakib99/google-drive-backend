from abc import ABC, abstractmethod
from typing import Callable
from common.models.dependencies_model import CommonDependenciesModel

class InterceptorABC(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def intercept(self,next: Callable, dependencies:CommonDependenciesModel, *args, **kwargs):
        pass