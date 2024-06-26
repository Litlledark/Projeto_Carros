from sqlalchemy import Column, Integer, String
from database import Base


class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    ano = Column(Integer)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
