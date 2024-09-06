from fastapi import FastAPI, APIRouter
from fastapi.middleware import gzip, cors
from dotenv import load_dotenv
from database_service.service import DatabaseService
from user_service.route import router as user_router

async def lifespan(app):
    load_dotenv()
    DatabaseService(None).connect()
    yield
    DatabaseService(None).disconnect()

app = FastAPI(lifespan=lifespan)

routers: list[APIRouter] = [user_router]

for router in routers:
    app.include_router(router)

app.add_middleware(gzip.GZipMiddleware, minimum_size=1000, compresslevel=5)
app.add_middleware(cors.CORSMiddleware, 
    allow_origins = ['*'], 
    allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
    allow_headers = ['*'])



