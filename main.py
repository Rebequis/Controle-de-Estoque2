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


def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    nome_for = input('Nome do fornecedor: ').strip()
    nome_pro = input('Nome do produto: ').strip()

    ja_existe = False
    for p in produtos:
        if p['fornecedor'].lower() == nome_for.lower() and p['produto'].lower() == nome_pro.lower():
            ja_existe = True
            break

    if ja_existe:
        print('\n❌ Produto já cadastrado para este fornecedor!')
    else:
        try:
            qtd_inicial = int(input('Quantidade inicial em estoque: '))
        except ValueError:
            print('Quantidade inválida! Definida como 0.')
            qtd_inicial = 0

        novo_produto = {
            "fornecedor": nome_for,
            "produto": nome_pro,
            "quantidade": qtd_inicial
        }
        produtos.append(novo_produto)
        print('\n✅ Produto cadastrado com sucesso!')
