from database_service.mysql_service import MySQLService
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from file_service.schemas.file_schema import FileSchema
from datetime import datetime

Base = MySQLService.get_base()

class UserSchema(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    password_reset_token = Column(String(255), nullable=True)
    password_reset_token_generated_at = Column(DateTime, nullable=False)
    profile_picture_id = Column(Integer, ForeignKey('FileSchema'))
    is_active = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    profile_picture = relationship('FileSchema')
