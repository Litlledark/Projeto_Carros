# crud.py
from sqlalchemy.orm import Session
import models  # Modificado: importação absoluta

def get_carros(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Carro).offset(skip).limit(limit).all()

def get_carro(db: Session, carro_id: int):
    return db.query(models.Carro).filter(models.Carro.id == carro_id).first()

def create_carro(db: Session, carro: models.Carro):
    db.add(carro)
    db.commit()
    db.refresh(carro)
    return carro

def update_carro(db: Session, carro_id: int, marca: str, modelo: str, ano: int):
    carro = db.query(models.Carro).filter(models.Carro.id == carro_id).first()
    carro.marca = marca
    carro.modelo = modelo
    carro.ano = ano
    db.commit()
    return carro

def delete_carro(db: Session, carro_id: int):
    carro = db.query(models.Carro).filter(models.Carro.id == carro_id).first()
    db.delete(carro)
    db.commit()
    return carro
