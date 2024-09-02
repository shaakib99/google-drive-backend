from database_service.mysql_service import MySQLService
from sqlalchemy import Column, Integer, String, Boolean

Base = MySQLService.get_instance().base

class UserSchema(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    password_reset_token = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)