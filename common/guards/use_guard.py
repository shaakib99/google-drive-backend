from common.guards.lib.abcs.guard_abc import GuardABC
from typing import Callable
from functools import wraps

class UseGuard:
    def __init__(self, guard: GuardABC):
        self.guard = guard
    
    def __call__(self, func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            dependecies = kwargs.get('CommonDependencies')
            await self.guard.dispatch(dependecies)
            return await func(*args, **kwargs)
        return wrapper