from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:pme-03@10.0.12.57:35096/teste"
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = 'SIZH5iSvo4OcTFZi9pCLgdxtJtwLD6997lU83IuSgwc'
    # import secrets
    # token: str = secrets.token_urlsafe(32)
    ALGORITHM: str = 'HS256'
    
    ACCES_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()