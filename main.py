import os


def limpar_tela():

    os.system('cls' if os.name == 'nt' else 'clear')


def Menu():
    print("""
========================= MENU =======================
 1-> Cadastrar produto
 2-> Listar Produtos
 3-> Atualizar Quantidade dos Produtos
 4-> Remover Produto
 5-> Consultar Estoque
 6-> Sair
------------------------------------------------------""")
