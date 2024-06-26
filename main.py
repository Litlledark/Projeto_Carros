# main.py
import database
import crud
import models
from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import sys
import codecs


# Resto do código...


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

templates = Jinja2Templates(directory="templates")

# Adicionar middleware CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(database.get_db)):
    carros = crud.get_carros(db)
    return templates.TemplateResponse("index.html", {"request": request, "carros": carros})


@app.post("/carros/")
def create_carro(marca: str = Form(...), modelo: str = Form(...), ano: int = Form(...), db: Session = Depends(database.get_db)):
    carro = models.Carro(marca=marca, modelo=modelo, ano=ano)
    db_carro = crud.create_carro(db=db, carro=carro)
    return db_carro


@app.get("/carros/{carro_id}")
def read_carro(carro_id: int, db: Session = Depends(database.get_db)):
    db_carro = crud.get_carro(db, carro_id=carro_id)
    if db_carro is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_carro


@app.put("/carros/{carro_id}")
def update_carro(carro_id: int, marca: str = Form(...), modelo: str = Form(...), ano: int = Form(...), db: Session = Depends(database.get_db)):
    carro = crud.get_carro(db, carro_id=carro_id)
    if carro is None:
        raise HTTPException(status_code=404, detail="Car not found")
    carro = crud.update_carro(db, carro_id=carro_id,
                              marca=marca, modelo=modelo, ano=ano)
    return carro


@app.delete("/carros/{carro_id}")
def delete_carro(carro_id: int, db: Session = Depends(database.get_db)):
    carro = crud.get_carro(db, carro_id=carro_id)
    if carro is None:
        raise HTTPException(status_code=404, detail="Car not found")
    crud.delete_carro(db, carro_id=carro_id)
    return {"message": "Carro deletado com sucesso"}
