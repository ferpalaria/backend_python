from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class inscritos(Base):
    __tablename__ = "Inscritos"

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=True)
    evento_id = Column(Integer, ForeignKey("Eventos.id"))
