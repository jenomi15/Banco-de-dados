import mysql.connector
import sqlite3
from classes import Cliente, Filial, Produto, Vendedor, Gerente, Pagamento, Desconto, Pix, Cartao, ItemVenda
from funcoes import EMmassa, criar_gatilho_atualizar_salario_vendedor, busca_do_usuario_geral, busca_do_usuario_substring, busca_geral, deletar, \
    insere, VendasPorFilial, totalvendasvendedorcliente, atualizar_registro, produtos_preco_maior_que_todos_os_preco, \
    vendedores_com_vendas_superiores_a_precos_filial_id, group_by_having

# senha = (str(input("digite a senha")))
conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="loja_guy"
)
# cursor = conexao.cursor()
# tabela = (str(input("digite a tabela")))
# query = f"SELECT * FROM `{tabela}`"
# cursor.execute(query)
# meuresultado = cursor.fetchall()
# for i in meuresultado:
# print(i)
# nome = input("Digite o nome do cliente: ").strip()
# insert_query = "INSERT INTO Cliente (Nome) VALUES (%s)"
# cursor.execute(insert_query, (nome,))
# conexao.commit()
# cursor.close()
# conexao.close()
tabelas = {
    "Cliente": Cliente,
    "Filial": Filial,
    "Produto": Produto,
    "Vendedor": Vendedor,
    "Pagamento": Pagamento,
    "Desconto": Desconto,
    "Pix": Pix,
    "Cartao": Cartao,
    "ItemVenda": ItemVenda,
    "Gerente": Gerente
}


def main():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="loja_guy"
    )

    print(
        "                    ------------------- BEM VINDO AO SISTEMA DO BANCO DE DADOS DA LOJA GUY -------------------\n")
    i = "sim"
    print("                              ------------------- OPÇÕES DE CONSULTA -------------------")
    while i == "sim":
        print(
            " 1- Inserir dados\n 2- Pesquisar dados\n 3- Atualizar dados\n 4- Deletar dados\n 5- Inserir vários tipos de dados\n "
            "6- Buscar dados por palavra chave (substring)\n 7- Total de vendas realizadas por cada vendedor para cada cliente\n 8- Vendas por filial\n 9- Produtos com o preço maior que todos os preços de uma filial\n 10- Vendedores com vendas de valor superior aos produtos de alguma filial\n "
            "11- criar gatilho que atualiza os salarios dos vendedores \n 12- Consulta por Agrupamento")
        escolha = input("digite a opção desejada\n")
        if escolha == "1":
            insere(conexao) # ok
        elif escolha == "2":
            busca_do_usuario_geral(conexao) # ok
        elif escolha == "3":
            atualizar_registro(conexao) # ok
        elif escolha == "4":
            deletar(conexao) # ok
        elif escolha == "5":
            EMmassa(conexao) # ok
        elif escolha == "6":
            busca_do_usuario_substring(conexao) # ok
        elif escolha == "7":
            totalvendasvendedorcliente(conexao) # ok
        elif escolha == "8":
            VendasPorFilial(conexao) # ok
        elif escolha == "9":
            produtos_preco_maior_que_todos_os_preco(conexao) # ok
        elif escolha == "10":
            vendedores_com_vendas_superiores_a_precos_filial_id(conexao) # ok
        elif escolha == "11":
            criar_gatilho_atualizar_salario_vendedor(conexao) # ok
        elif escolha == "12":
            group_by_having(conexao) # ok
        i = input("deseja continuar?\n\n\n")
    # totalvendasvendedorcliente(conexao)
    # VendasPorFilial(conexao)
    # insere(conexao)
    # deletar(conexao)
    # EMmassa(conexao)
    # buscar(conexao)
    # busca_do_usuario(conexao)
    # atualizar_registro(conexao)
    # produtos_preco_maior_que_todos_os_preco(conexao)
    # vendedores_com_vendas_superiores_a_precos_filial_id(conexao)



main()

