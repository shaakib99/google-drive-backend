from common.guards.lib.abcs.guard_abc import GuardABC
from typing import Callable
from functools import wraps
from common.models.dependencies import CommonDependencies




class UseGuard:
    def __init__(self, guard: GuardABC):
        self.guard = guard
    
    def __call__(self, func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            dependecies = kwargs.get('CommonDependencies')
            result = await self.guard.dispatch(dependecies)
            if isinstance(result, tuple):
                kwargs.__setattr__(tuple[0], tuple[1])
            return await func(*args, **kwargs)
        return wrapper