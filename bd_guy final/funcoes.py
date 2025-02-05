import mysql.connector
from classes import Filial, Gerente, Vendedor, Produto, Cliente, Pagamento, Desconto, Pix, Cartao, ItemVenda
import tkinter as tk

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password= "Mestrepokemon2006#" ,
    database="loja_guy"
)


def EMmassa(conexao):
    janela = tk.Tk()
    janela.title("procurando em massa")
    janela.geometry("400x300")
    frame_massa = tk.Frame(janela)
    frame_massa.pack(fill="both", expand=True)
    if not conexao.is_connected():
        print("fazendo a conexao")
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Mestrepokemon2006#",
            database="loja_guy"
        )

    print("\nTabelas disponíveis:")
    tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda"]
    lista_objetos = []
    
    for i in tabelas:
        print(f"tabela {i}")
        j = (int(input(f"digite a quantidade de elementos desejados para a tabela {i} ")))
        for x in range(j):
            if i == "Cliente":
                print("digite os atributos do cliente desejado")
                nome = input("digite o nome do cliente").strip()
                clientenovo = Cliente(nome=nome)
                lista_objetos.append(clientenovo)
            elif i == "Filial":
                print("digite as filiais desejadas")
                localizacao = input("digite a localização").strip()
                filialnova = Filial(localizacao=localizacao)
                lista_objetos.append(filialnova)
            elif i == "Produto":
                print("digite o produto desejado")
                nome = input("digite o nome do produto").strip()
                preco = input("digite o preço do produto").strip()
                produtonovo = Produto(nome=nome, preco=preco)
                lista_objetos.append(produtonovo)
            elif i == "Vendedor":
                print("digite o vendedor desejado")
                nome = input("digite o nome do vendedor").strip()
                id_gerente = input("digite o id do gerente relacionado").strip()
                id_filial = input("digite o id da filial relacionada").strip()
                vendedornovo = Vendedor(nome=nome, id_gerente=id_gerente, id_filial=id_filial)
                lista_objetos.append(vendedornovo)
            elif i == "pagamento":
                print("digite o pagamento desejado")
                id_cliente = input("digite o id do cliente relacionado")
                valor_total = input("digite o valor total do pagamento")
                pagamentonovo = Pagamento(id_cliente=id_cliente, valor_total=valor_total)
                lista_objetos.append(pagamentonovo)
            elif i == "Desconto":
                print("digite o desconto desejado")
                id_pagamento = input("id pagamento relacionado")
                valor_desconto = input("digite o valor do desconto aplicado")
                descontonovo = Desconto(id_pagamento=id_pagamento, valor_desconto=valor_desconto)
                lista_objetos.append(descontonovo)
            elif i == "Pix":
                print("digite o pix desejado")
                id_pagamento = input("digite o pagamento relacionado")
                banco = input('digite o nome do banco ')
                pixnovo = Pix(id_pagamento=id_pagamento, banco=banco)
                lista_objetos.append(pixnovo)
            elif i == "Cartao":
                print("digite o cartao desejado")
                id_pagamento = input("digite o pagamento relacionado")
                parcelas = input("digite a quantidade de parcelas")
                cartaonovo = Cartao(id_pagamento=id_pagamento, parcelas=parcelas)
                lista_objetos.append(cartaonovo)
            elif i == "ItemVenda":
                print("digite a linha da tabela item venda desejada")
                nome_produto = input("digite o nome do produto relacionado ")
                quantidade = input("digite a quantidade")
                id_vendedor = input("digite o id do vendedor relacionado")
                id_cliente = input("digite o id do cliente relacionado")
                itemvendanovo = ItemVenda(nome_produto=nome_produto, quantidade=quantidade, id_vendedor=id_vendedor, id_cliente=id_cliente)
                lista_objetos.append(itemvendanovo)
    
    for y in lista_objetos:
        y.inserir(conexao)


def buscar(conexao):
    tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda"]
    for i in tabelas:
        print(i)         
    tabelaescolhida = input("Escolha uma das tabelas: ")
    if tabelaescolhida not in tabelas:
        print("Tabela inválida, por favor escolha uma tabela da lista.")
        return
    listadecolunas = []
    listadeclausulas = []
    i = "sim"
    k = "sim"
    while i == "sim":
        j = input("Digite as colunas que você quer inserir na busca: ")
        listadecolunas.append(j)
        i = input("Você deseja continuar (sim/nao)? ")
    while k == "sim":
        o = input("Digite as cláusulas para a busca: ")
        listadeclausulas.append(o)
        k = input("Você deseja continuar (sim/nao)? ")
    if "*" not in listadecolunas:
        listadecolunas1 = ",".join(listadecolunas) 
    else:
        listadecolunas1 = "*"
    if "nenhuma" not in listadeclausulas:
        listadeclausulas1 = " AND ".join(listadeclausulas)
        query = f"SELECT {listadecolunas1} FROM {tabelaescolhida} WHERE {listadeclausulas1}"
        print(query)
    else:
        query = f"SELECT {listadecolunas1} FROM {tabelaescolhida}"  
        print(query)
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()  
        print(resultados)
    except Exception as e: 
        print(e)
    finally:
        cursor.close()




def busca_geral(conexao, tabela, condicao=None, nome_coluna=None):
    cursor = conexao.cursor()
    try:
        # Se a coluna for fornecida, ajusta a condição
        if nome_coluna:
            if condicao:
                # Se a condição foi fornecida, monta a query com a coluna e a condição
                query = f"SELECT {nome_coluna} FROM {tabela} WHERE {condicao} "
                print(query)
            else:
                # Se não houver condição, monta a query apenas com a coluna
                query = f"SELECT {nome_coluna} FROM {tabela} "
        else:
            # Caso contrário, é apenas uma busca geral com a condição
            if condicao:
                query = f"SELECT * FROM {tabela} WHERE {condicao}"
            else:
                query = f"SELECT * FROM {tabela}"

        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print(f"Erro ao buscar dados da tabela {tabela}: {e}")
    finally:
        cursor.close()


def busca_do_usuario(conexao):
    try:
        # Solicita ao usuário o nome da tabela
        tabela = input("Digite o nome da tabela que deseja pesquisar: ")
        # Solicita ao usuário a coluna para o filtro (deixa em branco se não quiser filtrar por coluna específica)
        nome_coluna = input("Deseja filtrar por uma coluna específica? (Digite o nome da coluna ou pressione Enter para continuar): ")
        condicao = input("Deseja adicionar uma condição para filtrar os dados? (ex: id_cliente = 45 ou salario > 2000)\nDigite a condição ou pressione Enter para continuar sem filtro: ")

        # Verifica se a condição está no formato correto
        if condicao:
            if "=" not in condicao:
                print("Formato inválido para a condição. A condição deve ser no formato 'coluna = valor'.")
                return

        # Chama a função de busca geral passando a condição ajustada
        resultados = busca_geral(conexao, tabela, condicao if condicao else None, nome_coluna if nome_coluna else None)

        if resultados:
            print(f"Dados encontrados: {resultados}")
        else:
            print("Nenhum dado encontrado na tabela com essa condição.")

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ou buscar dados no banco de dados: {err}")
    finally:
       conexao.close()