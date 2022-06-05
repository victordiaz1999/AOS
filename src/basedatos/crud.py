import models
import schemas
from sqlalchemy.orm import Session


def get_cliente_by_id(db: Session, id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == id).first()

def get_cliente_by_nif(db: Session, nif: str):
    return db.query(models.Cliente).filter(models.Cliente.nif == nif).first()

def get_cliente_by_nombre(db:Session, nombre: str):
    return db.query(models.Cliente).filter(models.Cliente.nombre == nombre).first()

def get_clientes(db: Session,skip: int=0,limit: int=100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def deleteCliente(db: Session, idCliente: int):
    db.query(models.Cliente).filter(models.Cliente.idCliente == idCliente).delete()
    db.commit()
    return 0