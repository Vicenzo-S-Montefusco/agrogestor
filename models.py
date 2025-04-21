# models.py
from sqlalchemy import Identity, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    
    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True)
    nome = Column(String(100))
    funcao = Column(String(100))