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

class Talhoes(Base):
    __tablename__ = 'talhoes'

    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True)
    nome = Column(String(100), nullable=False)
    area = Column(Float, nullable=False)
    cultura = Column(String(100), nullable=False)
    data_plantio = Column(Date, nullable=True)
    data_colheita = Column(Date, nullable=True)

class Financeiros(Base):
    __tablename__ = 'financeiro'

    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True)
    descricao = Column(String(200), nullable=False)
    tipo_movimentacao = Column(String(50), nullable=False)  # 'receita' ou 'despesa'
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)

class Relatorios(Base):
    __tablename__ = 'relatorios'

    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True)
    nome = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)   # ex: 'vendas', 'estoque', etc.
    descricao = Column(String(200), nullable=True)
    data_geracao = Column(Date, nullable=False)

class Tarefas(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, Identity(start=1, cycle=False), primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(300), nullable=True)
    status = Column(String(50), nullable=False)  # ex: 'pendente', 'em andamento', 'concluída'
    data_inicio = Column(Date, nullable=True)
    data_conclusao = Column(Date, nullable=True)