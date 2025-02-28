from sqlmodel import SQLModel, Field, create_engine
from datetime import date
from enum import Enum

class Autores(Enum):
    AGATHA_CHISTIE = 'Agatha Chistie'
    STEPHEN_KING = 'Stephen King'
    MACHADO_DE_ASSIS = 'Machado De Assis'
    CLARICE_LISPECTOR = 'Clarice Lispector'
    WILLIAM_SHAKESPEARE = 'William Shakespeare'

class Paises(Enum):
    REINO_UNIDO = 'Reino Unido'
    BRASIL = 'Brasil'
    ESPANHA = 'Espanha'
    ESTADOS_UNIDOS = 'Estados Unidos'

class Genero(Enum):
    FANTASIA = 'Fantasia'
    TERROR = 'Terror'
    ROMANCE = 'Romance'
    MISTERIO = 'Misterio'
    AVENTURA = 'Aventura'

class Livros(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str = Field(max_length=70)
    numero_paginas: int
    autor: Autores = Field(default=Autores.CLARICE_LISPECTOR)
    nacionalidade: Paises = Field(default=Paises.ESPANHA)
    genero: Genero = Field(default=Genero.ROMANCE)
    data: date

database = 'database.db'
url = f"sqlite:///{database}"

engine = create_engine(url, echo=False)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)