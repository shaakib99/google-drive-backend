from fastapi import Request
from common.models.dependencies import CommonDependencies

def inject_common_dependencies(request: Request) -> CommonDependencies:
    dependencies = CommonDependencies(request=request)
    return dependencies