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


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            lista = arquivo.read().splitlines()

            if not lista:
                print('Arquivo vazio')
                return None
            else:
                return lista
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return None
