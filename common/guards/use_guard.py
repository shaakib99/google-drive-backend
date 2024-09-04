from common.lib.abcs.guard_abc import GuardABC
from fastapi import Request, Response

class UseGuard:
    def __init__(self, guard: GuardABC):
        self.guard = guard
    
    def __call__(self, req: Request, res: Response):
        return self.guard.invoke_guard(req, res)