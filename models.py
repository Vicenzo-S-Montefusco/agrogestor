# models.py
from sqlalchemy import Identity, Float, Date, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    
    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True)
    nome = Column(String(100), nullable=False)
    funcao = Column(String(100), nullable=False)

class Insumos(Base):
    __tablename__ = 'insumos'
    
    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True)
    nome = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    data_validade = Column(Date, nullable=False)