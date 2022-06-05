from typing import TypedDict, Union
from pydantic import BaseModel, Field

class Cliente(BaseModel):
    idCliente: int
    nif: str
    nombre: str
    apellidos: str
    telefono: str
    domicilio: str
    email: str

class ClienteUpdate(BaseModel):
    idCliente: Union[int, None] = Field(ge=0)
    nif: Union[str, None] = None
    nombre: Union[str, None] = None
    apellidos: Union[str, None] = None
    telefono: Union[str, None] = None
    domicilio: Union[str, None] = None
    email: Union[str, None] = None


