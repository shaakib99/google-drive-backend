from abc import ABC, abstractmethod
from typing import Callable
from common.models.dependencies import CommonDependencies

class InterceptorABC(ABC):
    def __init__(self):
        pass

    @abstractmethod
    async def intercept(self,next: Callable, dependencies:CommonDependencies, *args, **kwargs):
        pass