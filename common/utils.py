from fastapi import Request
from common.models.dependencies_model import CommonDependenciesModel
import json

def inject_common_dependencies(request: Request) -> CommonDependenciesModel:
    dependencies = CommonDependenciesModel(request=request)
    return dependencies

def generate_cache_key(key: str, prefix: str, params: str) -> str:
    return f"{prefix}{key}{params}"