from sqlalchemy import Column, Integer, String

from .database import Base




class Cliente(Base):
    __tablename__ = "clientes"
    idCliente = Column(Integer, primary_key=True, index=True)
    nif = Column(String, nullable=False)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(50))
    telefono = Column(String(50))
    domicilio = Column(String(50))
    email = Column(String(50))





