from fastapi import Request, Response
from common.models.dependencies_model import CommonDependenciesModel
from cryptography.fernet import Fernet
import bcrypt
import string
import random
import os

def inject_common_dependencies(request: Request, response: Response) -> CommonDependenciesModel:
    dependencies = CommonDependenciesModel(request=request, response = response)
    return dependencies

def generate_cache_key(key: str, prefix: str, params: str) -> str:
    return f"{prefix}{key}{params}"

def generate_random_characters(length, include_digits = True, include_lower_case = True, include_upper_case = True):
    choices = ''
    if include_digits:
        choices += string.digits
    
    if include_lower_case:
        choices += string.ascii_lowercase
    
    if include_upper_case:
        choices += string.ascii_uppercase

    return ''.join(random.SystemRandom().choice(choices) for _ in range(length))

def encrypt(data: str, secret = os.getenv('ENCRYPT_SECRET')) -> str:
    fernet = Fernet(secret)
    return fernet.encrypt(data.encode()).decode()

def decrypt(encrypted_data: str, secret = os.getenv('ENCRYPT_SECRET')) -> str:
    fernet = Fernet(secret)
    return fernet.decrypt(encrypted_data.encode()).decode()

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), os.getenv('BCRYPT_SALT') )