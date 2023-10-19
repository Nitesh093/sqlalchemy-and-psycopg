from django.apps import AppConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # Assuming your SQLAlchemy models are defined in models.py

class CitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cities'

    
