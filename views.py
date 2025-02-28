from models import Livros, engine
from sqlmodel import Session, select
from datetime import date

def criar_livro(livro: Livros):
    with Session(engine) as session:
        statement = select(Livros).where(Livros.nome==livro.nome)
        results = session.exec(statement).all()
        
        if results:
            raise ValueError('Já existe um livro com esse nome')
        
        session.add(livro)
        session.commit()
        return livro

def listar_livros():
    with Session(engine) as session:
        statement = select(Livros)
        results = session.exec(statement).all()
        
        print('---Nome dos livros---\n')
        for resultado in results:
            print(resultado.nome)

def atualizar_livro(id, nome):
    with Session(engine) as session:
        statement = select(Livros).where(Livros.id==id)
        results = session.exec(statement).first()
        
        if nome != results.nome:
            results.nome = nome
        else:
            raise ValueError('O nome desse livro já existe')
            
        session.commit()
        return results

def deletar_livro(id):
    with Session(engine) as session:
        statement = select(Livros).where(Livros.id==id)
        results = session.exec(statement).first()
        session.delete(results)
        session.commit()

def total_paginas():
    with Session(engine) as session:
        statement = select(Livros)
        results = session.exec(statement).all()
        
    total = 0
    for result in results:
        total += result.numero_paginas
    return f"O número total de páginas de todos os livros é {total} páginas"

def grafico():
    with Session(engine) as session:
        statement = select(Livros)
        livros = session.exec(statement).all()
        generos = [i.genero.value for i in livros]
        paginas = [i.numero_paginas for i in livros]
        
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.pie(paginas, labels=generos, autopct='%1.1f%%')
        plt.show()

def historico_livros_criados(data_inicio: date, data_fim: date):
    with Session(engine) as session:
        statement = select(Livros).where(
            Livros.data >= data_inicio,
            Livros.data <= data_fim
        )
        results = session.exec(statement).all()
        return results
