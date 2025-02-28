from models import *
from views import *
from datetime import datetime
import re

class Interface():
    def iniciar(self):
        while True:
            print('''
            (1) => Criar livro
            (2) => Listar livros
            (3) => Atualizar livro
            (4) => Deletar livro
            (5) => Total de páginas de todos os livros
            (6) => Gráfico
            (7) => Histórico de livros criados\n''')
            
            escolha = str(input('Escolha alguma das opções anteriores: '))

            padrao = r'^[1-7]{1}$'
            
            verifica_escolha_user = re.fullmatch(padrao, escolha)
            if not verifica_escolha_user:
                print('Escolha inválida. Precisa ser um número inteiro entre 1 e 7')
            
            if escolha == '1':
                self._criar_livro()
            elif escolha == '2':
                self._listar_livros()
            elif escolha == '3':
                self._atualizar_livro()
            elif escolha == '4':
                self._deletar_livro()
            elif escolha == '5':
                self._total_paginas()
            elif escolha == '6':
                self._grafico()
            elif escolha == '7':
                self._historico_livros()
            else:
                break
            
    def _criar_livro(self):
        nome = input('Nome do livro: ').title()
        numero_paginas = int(input('Número de páginas: '))
        data = date.today()
        
        livro = Livros(nome=nome, numero_paginas=numero_paginas, data=data)
        criar_livro(livro)
    
    def _listar_livros(self):
        listar_livros()
        
    def _atualizar_livro(self):
        nome = input('Digite o nome do novo livro: ').title()
        id_livro = int(input('Digite o número do id do livro que será modificado: '))
        
        atualizar_livro(id=id_livro, nome=nome)
        
    def _deletar_livro(self):
        id = int(input('Digite o número do id para deletar um livro: '))
        deletar_livro(id)
        
    def _total_paginas(self):
        print(f"{total_paginas()}")
        
    def _grafico(self):
        grafico()
    
    def _historico_livros(self):
        data_inicio = input('Data de início: ')
        data_fim = input('Data de fim: ')
        
        data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()
        
        print(f'Livros cadastrados entre as datas: {data_inicio} e {data_fim}')
        for i in historico_livros_criados(data_inicio, data_fim):
            print(f"{i.nome} - {i.autor.value} - {i.genero.value}\n")

Interface().iniciar()