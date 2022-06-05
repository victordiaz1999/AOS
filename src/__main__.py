from fastapi import Depends, FastAPI
import basedatos.models as models
import basedatos.crud as crud
import uvicorn
from sqlalchemy.orm import Session
from basedatos.database import  engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/cliente/{idCliente}")
async def read_item(idCliente: int):
    return {"idCliente": idCliente}

@app.get("cliente/{nif}")
def get_clientes_by_nif(idCliente: int, db: Session = Depends(get_db)):
    return crud.get_clientes_by_idCliente(db,idCliente=idCliente)

@app.get("cliente/{nif}")
def get_clientes_by_nif(nif: str, db: Session = Depends(get_db)):
    return crud.get_clientes_by_nif(db,nif=nif)

@app.get("cliente/{nombre}")
def get_clientes_by_nombre(nombre: str, db: Session = Depends(get_db)):
    return crud.get_clientes_by_nombre(db,nombre=nombre)

@app.get("/cliente/{}")
def get_clientes():
    return crud.get_clientes(Session, 0, 100)

@app.delete("/cliente/{idCliente}")
def delete_cliente(idCliente: int, db: Session = Depends(get_db())):
    return crud.deleteCliente(db, idCliente=idCliente)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8000")

