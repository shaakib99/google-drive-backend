from fastapi import Request
from common.models.dependencies_model import CommonDependenciesModel

def inject_common_dependencies(request: Request) -> CommonDependenciesModel:
    dependencies = CommonDependenciesModel(request=request)
    return dependencies