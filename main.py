from fastapi import FastAPI, APIRouter
from fastapi.middleware import gzip, cors
from dotenv import load_dotenv
from database_service.service import DatabaseService
from cache_service.service import CacheService
from user_service.route import router as user_router
from auth_service.route import router as auth_router
from common.middlewares.response_middleware import ResponseMiddleware

async def lifespan(app):
    load_dotenv()
    db_service = DatabaseService(None)
    db_service.connect()
    db_service.create_metadata()

    cache_service = CacheService()
    cache_service.connect()
    yield
    db_service.disconnect()
    cache_service.disconnect()

app = FastAPI(lifespan=lifespan)

routers: list[APIRouter] = [user_router, auth_router]

for router in routers:
    app.include_router(router)

app.add_middleware(gzip.GZipMiddleware, minimum_size=1000, compresslevel=5)
app.add_middleware(cors.CORSMiddleware, 
    allow_origins = ['*'], 
    allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
    allow_headers = ['*'])
# custom middlewares
app.add_middleware(ResponseMiddleware)



