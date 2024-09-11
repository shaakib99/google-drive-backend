from database_service.mysql_service import MySQLService
from sqlalchemy import Integer, Column, String, Boolean, DateTime
from datetime import datetime

Base = MySQLService.get_base()

class FileSchema(Base):
    __tablename__ = 'files'

    id = Column(Integer(), autoincrement=True, primary_key=True, nullable = False)
    url = Column(String(length=300), nullable = False)
    provider = Column(String(length=10), nullable = False)
    mimetype = Column(String(length=20), nullable = True)
    is_deleted = Column(Boolean(), nullable=False, default=False)
    created_date = Column(DateTime, nullable=False, default=datetime.now())