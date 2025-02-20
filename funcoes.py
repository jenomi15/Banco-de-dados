import mysql.connector
from classes import Filial, Gerente, Vendedor, Produto, Cliente, Pagamento, Desconto, Pix, Cartao, ItemVenda
from datetime import  datetime

conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="loja_guy"
)


def EMmassa(conexao):
    # testa a conexao com o bd
    if not conexao.is_connected():
        print("fazendo a conexao")
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="loja_guy"
        )

    tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda",
               "Gerente"]
    lista_objetos = []

    for i in tabelas:
        print(f"tabela {i}") # printa a tabela iterada
        j = (int(input(f"digite a quantidade de elementos desejados para a tabela {i} "))) # recebe a qnt de elementos na tabela atual
        for x in range(j):
            if i == "Cliente": # Verifica qual a tabela estamos iterando e recebe os dados para seus atributos
                print("digite os atributos do cliente desejado")
                nome = input("digite o nome do cliente").strip()
                telefone = input("digite o telefone do cliente (enter: pular)").strip()
                datadeentrada = input("digite a data de entrada do cliente (enter: data atual").strip()
                endereco = input("digite o endereco do cliente(enter: pular)").strip()
                clientenovo = Cliente(nome=nome, telefone=telefone, datadeentrada=datadeentrada, endereco=endereco) # Cria um objeto da tabela em questão e apenda ele na lista de objetos
                lista_objetos.append(clientenovo)
            elif i == "Filial":
                print("digite as filiais desejadas")
                localizacao = input("digite a localização").strip()
                tempodeparceria = input("digite o tempo de parceria (enter: data atual)").strip()
                telefone = input("digite o telefone do cliente (enter : pular)").strip()
                nome = input("digite o nome da filial  (enter : pular) ").strip()

                filialnova = Filial(localizacao=localizacao, tempodeparceria=tempodeparceria, telefone=telefone,
                                    nome=nome)
                lista_objetos.append(filialnova)
            elif i == "Produto":
                print("digite o produto desejado")
                nome_produto = input("digite o nome do produto").strip()
                preco = input("digite o preço do produto").strip()
                datadecriacao = input("digite a data de criacao (enter = data atual)").strip()
                tamanho = input("digite o tamanho (enter : pular)").strip()
                nicho = input("digite o nicho do produto (enter: pular)").strip()
                id_filial = input("digite a filial a ual o produto vai estar relacionada").strip()
                produtonovo = Produto(nome_produto=nome_produto, preco=preco, tamanho=tamanho,
                                      datadecriacao=datadecriacao, nicho=nicho, id_filial=id_filial)
                lista_objetos.append(produtonovo)
            elif i == "Vendedor":
                print("digite o vendedor desejado")
                nome = input("digite o nome do vendedor").strip()
                id_gerente = input("digite o id do gerente relacionado").strip()
                id_filial = input("digite o id da filial relacionada").strip()
                datadeentrada = input("digite a data de entrada da filial (enter: data atual)").strip()
                telefone = input("digite o telefone do vendedro (enter: pular)").strip()
                salario = input("digite o salario do vendedor (enter : pular)").strip()
                vendedornovo = Vendedor(nome=nome, id_gerente=id_gerente, id_filial=id_filial,
                                        datadeentrada=datadeentrada, salario=salario, telefone=telefone)
                lista_objetos.append(vendedornovo)
            elif i == "pagamento":
                print("digite o pagamento desejado")
                id_cliente = input("digite o id do cliente relacionado").strip()
                valor_total = input("digite o valor total do pagamento").strip()
                banco = input("digite o nome do banco (enter : pular)").strip()
                datapagamento = input("digite a data do pagamento (enter : data atual)").strip()
                aprovado = input("digite se o pagamento foi aprovado ou nao").strip()
                pagamentonovo = Pagamento(id_cliente=id_cliente, valor_total=valor_total, banco=banco,
                                          datapagamento=datapagamento, aprovado=aprovado)
                lista_objetos.append(pagamentonovo)
            elif i == "Desconto":
                print("digite o desconto desejado")
                id_pagamento = input("id pagamento relacionado").strip()
                valor_desconto = input("digite o valor do desconto aplicado").strip()
                descontonovo = Desconto(id_pagamento=id_pagamento, valor_desconto=valor_desconto)
                lista_objetos.append(descontonovo)
            elif i == "Pix":
                print("digite o pix desejado")
                id_pagamento = input("digite o pagamento relacionado").strip()
                banco = input('digite o nome do banco ').strip()
                pixnovo = Pix(id_pagamento=id_pagamento, banco=banco)
                lista_objetos.append(pixnovo)
            elif i == "Cartao":
                print("digite o cartao desejado")
                id_pagamento = input("digite o pagamento relacionado").strip()
                parcelas = input("digite a quantidade de parcelas").strip()
                cartaonovo = Cartao(id_pagamento=id_pagamento, parcelas=parcelas)
                lista_objetos.append(cartaonovo)
            elif i == "ItemVenda":
                print("digite a linha da tabela item venda desejada")
                nome_produto = input("digite o nome do produto relacionado ").strip()
                quantidade = input("digite a quantidade").strip()
                id_vendedor = input("digite o id do vendedor relacionado").strip()
                id_cliente = input("digite o id do cliente relacionado").strip()
                itemvendanovo = ItemVenda(nome_produto=nome_produto, quantidade=quantidade, id_vendedor=id_vendedor,
                                          id_cliente=id_cliente)
                lista_objetos.append(itemvendanovo)
            elif i == "Gerente":
                print("digite o gerente desejado")
                nome = input("digite o nome do gerente").strip()
                tempoemgerencia = input("digite o tempo em gerencia (enter = horário atual)").strip()
                telefone = input("digite o telefone (enter : pular)").strip()
                numerofunc = input("digite o numero de funcionarios ( enter : pular)").strip()
                gerentenovo = Gerente(nome=nome, tempoemgerencia=tempoemgerencia, telefone=telefone,
                                      numerofunc=numerofunc)
                lista_objetos.append(gerentenovo)

    # Insere cada elemento da lista de objetos na database
    for y in lista_objetos:
        y.inserir(conexao)


def deletar(conexao):
    tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda",
               "Gerente"]

    for i in tabelas:
        print(i)

    tabelaescolhida = input("digite a tabela escolhida")

    if tabelaescolhida not in tabelas:
        print("tabela nao existe , por favor escolha outra da lista")
        return

    listadeclausulas = []

    k = "sim"

    # Loop para receber as cláusulas para deletar
    while k == "sim" or k == "s":
        o = input("Digite as cláusulas para a delecao (Salario > 1000: ")
        listadeclausulas.append(o)
        k = input("Você deseja continuar (sim/nao)? ")

    # Verifica se há alguma cláusula selecionada para deletar
    if "nenhuma" not in listadeclausulas:
        listadeclausulas1 = " AND ".join(listadeclausulas)
        query = f"DELETE FROM {tabelaescolhida} WHERE {listadeclausulas1}"
        print(query)
    # Se não, deleta todas as colunas
    else:
        query = f"DELETE FROM {tabelaescolhida}"
        print(query)

    # Try catch para realizar as mudanças no bd
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()


def insere(conexao):
    if not conexao.is_connected():
        print("fazendo a conexao")
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="loja_guy"
        )

    print("\nTabelas disponíveis:")
    tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda",
               "Gerente"]

    for i in tabelas:
        print(f"tabela {i}")

    j = input("digite a tabela desejada para inserir ").strip()

    while j not in tabelas:
        j = input("errr tabela nao existente , escreva dnv chapa: ").strip()

    # Condicionais que verifical qual tabela vamos inserir o novo elemento

    if j == "Cliente":
        print("digite os atributos do cliente desejado")
        nome = input("digite o nome do cliente").strip()
        telefone = input("digite o telefone do cliente (enter: pular)").strip()
        datadeentrada = input("digite a data de entrada do cliente (enter: data atual)").strip()
        endereco = input("digite o endereco do cliente(enter: pular)").strip()
        clientenovo = Cliente(nome=nome, telefone=telefone, datadeentrada=datadeentrada, endereco=endereco)
        clientenovo.inserir(conexao)

    elif j == "Filial":
        print("digite as filiais desejadas")
        localizacao = input("digite a localização").strip()
        tempodeparceria = input("digite o tempo de parceria (enter: data atual)").strip()
        telefone = input("digite o telefone do cliente (enter : pular)").strip()
        nome = input("digite o nome da filial  (enter : pular) ").strip()
        filialnova = Filial(localizacao=localizacao, tempodeparceria=tempodeparceria, telefone=telefone, nome=nome)
        filialnova.inserir(conexao)

    elif j == "Produto":
        print("digite o produto desejado")
        nome_produto = input("digite o nome do produto").strip()
        preco = input("digite o preço do produto").strip()
        datadecriacao = input("digite a data de criacao (enter = data atual)").strip()
        tamanho = input("digite o tamanho (enter : pular)").strip()
        nicho = input("digite o nicho do produto (enter: pular)").strip()
        id_filial = input("digite a filial a ual o produto vai estar relacionada").strip()
        produtonovo = Produto(nome_produto=nome_produto, preco=preco, tamanho=tamanho, datadecriacao=datadecriacao,
                              nicho=nicho, id_filial=id_filial)
        produtonovo.inserir(conexao)
    elif j == "Vendedor":
        print("digite o vendedor desejado")
        nome = input("digite o nome do vendedor").strip()
        id_gerente = input("digite o id do gerente relacionado").strip()
        id_filial = input("digite o id da filial relacionada").strip()
        datadeentrada = input("digite a data de entrada da filial (enter: data atual)").strip()
        telefone = input("digite o telefone do vendedor (enter: pular)").strip()
        salario = input("digite o salario do vendedor (enter : pular)").strip()
        vendedornovo = Vendedor(nome=nome, id_filial=id_filial, id_gerente=id_gerente, datadeentrada=datadeentrada, telefone=telefone, salario=salario)
        vendedornovo.inserir(conexao)

    elif j == "pagamento":
        print("digite o pagamento desejado")
        id_cliente = input("digite o id do cliente relacionado").strip()
        valor_total = input("digite o valor total do pagamento").strip()
        banco = input("digite o nome do banco (enter : pular)").strip()
        datapagamento = input("digite a data do pagamento (enter : data atual)").strip()
        aprovado = input("digite se o pagamento foi aprovado ou nao").strip()
        pagamentonovo = Pagamento(id_cliente=id_cliente, valor_total=valor_total, banco=banco,
                                  datapagamento=datapagamento, aprovado=aprovado)
        pagamentonovo.inserir(conexao)

    elif j == "Desconto":
        print("digite o desconto desejado")
        id_pagamento = input("id pagamento relacionado").strip()
        valor_desconto = input("digite o valor do desconto aplicado").strip()
        descontonovo = Desconto(id_pagamento=id_pagamento, valor_desconto=valor_desconto)
        descontonovo.inserir(conexao)

    elif j == "Pix":
        print("digite o pix desejado")
        id_pagamento = input("digite o pagamento relacionado").strip()
        banco = input("digite o nome do banco ").strip()
        pixnovo = Pix(id_pagamento=id_pagamento, banco=banco)
        pixnovo.inserir(conexao)

    elif j == "Cartao":
        print("digite o cartao desejado")
        id_pagamento = input("digite o pagamento relacionado").strip()
        parcelas = input("digite a quantidade de parcelas").strip()
        cartaonovo = Cartao(id_pagamento=id_pagamento, parcelas=parcelas)
        cartaonovo.inserir(conexao)

    elif j == "ItemVenda":
        print("digite a linha da tabela item venda desejada")
        nome_produto = input("digite o nome do produto relacionado ").strip()
        quantidade = input("digite a quantidade").strip()
        id_vendedor = input("digite o id do vendedor relacionado").strip()
        id_cliente = input("digite o id do cliente relacionado").strip()
        itemvendanovo = ItemVenda(nome_produto=nome_produto, quantidade=quantidade, id_vendedor=id_vendedor,
                                  id_cliente=id_cliente)
        itemvendanovo.inserir(conexao)

    elif j == "Gerente":
        print("digite o gerente desejado")
        nome = input("digite o nome do gerente").strip()
        tempoemgerencia = input("digite o tempo em gerencia (enter = horário atual)").strip()
        telefone = input("digite o telefone (enter : pular)").strip()
        numerofunc = input("digite o numero de funcionarios (enter : pular)").strip()
        gerentenovo = Gerente(nome=nome, tempoemgerencia=tempoemgerencia, telefone=telefone, numerofunc=numerofunc)
        gerentenovo.inserir(conexao)


def VendasPorFilial(conexao):
    print("Exibindo as vendas de cada filial")

    # Querry que faz Join com as tabelas Item_Venda, Vendedor e Filial. Relacionando os respectivos IDs de vendedor e filial
    query = """
        SELECT f.Localizacao AS Filial, SUM(iv.Quantidade) AS Total_Vendido
        FROM Item_Venda iv
        INNER JOIN Vendedor v ON iv.ID_Vendedor = v.ID_Vendedor
        INNER JOIN Filial f ON v.ID_Filial = f.ID_Filial
        GROUP BY f.Localizacao
        ORDER BY Total_Vendido DESC;
    """


    # Try catch para realizar as mudanças no bd
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(f"filial: {resultado[0]}, total Vendido: {resultado[1]}")
    except Exception as e:
        print(e)

    finally:
        cursor.close()


def busca_geral(conexao, tabela, condicao=None, nome_coluna=None):



    cursor = conexao.cursor()
    try:
        if nome_coluna:
            if condicao:

                query = f"SELECT {nome_coluna} FROM {tabela} WHERE {condicao} "
                print(query)
            else:

                query = f"SELECT {nome_coluna} FROM {tabela} "
        else:

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


def substring(conexao, tabela, nome_coluna, condicao):
    cursor = conexao.cursor()
    try:
        if nome_coluna:
            if condicao:

                query = f"SELECT {nome_coluna} FROM {tabela} WHERE {nome_coluna} LIKE {condicao} "
                print(query)
            else:

                query = f"SELECT {nome_coluna} FROM {tabela} "
        else:

            if condicao:
                query = f"SELECT * FROM {tabela} WHERE {nome_coluna} LIKE {condicao}"
            else:
                query = f"SELECT * FROM {tabela}"

        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print(f"Erro ao buscar dados da tabela {tabela}: {e}")
    finally:
        cursor.close()


def busca_do_usuario_geral(conexao):
    print("\nTabelas disponíveis:")
    tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda",
               "Gerente"]

    for i in tabelas:
        print(f"tabela {i}")

    try:

        tabela = input("Digite o nome da tabela que deseja pesquisar: ").lower().strip()

        # Solicita ao usuário a coluna para o filtro (deixa em branco se não quiser filtrar por coluna específica)
        nome_coluna = input("Deseja filtrar por uma coluna específica? (Digite o nome da coluna ou pressione Enter para continuar): ")
        condicao = input("Deseja adicionar uma condição para filtrar os dados? (ex: id_cliente = 45 ou salario > 2000)\nDigite a condição ou pressione Enter para continuar sem filtro: ")


        if condicao:
            if "=" not in condicao:
                print("Formato inválido para a condição. A condição deve ser no formato 'coluna = valor'.")
                return


        resultados = busca_geral(conexao, tabela, condicao if condicao else None, nome_coluna if nome_coluna else None)


        if resultados:
            print(f"Dados encontrados: {resultados}")
        else:
            print("Nenhum dado encontrado na tabela com essa condição.")

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ou buscar dados no banco de dados: {err}")
    finally:
       conexao.close()


def busca_do_usuario_substring(conexao):
    print("\nTabelas disponíveis:")
    tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda",
               "Gerente"]

    for i in tabelas:
        print(f"tabela {i}")

    try:

        tabela = input("Digite o nome da tabela que deseja pesquisar: ").lower()

        # Solicita ao usuário a coluna para o filtro (deixa em branco se não quiser filtrar por coluna específica)
        nome_coluna = input(
            "Deseja filtrar por uma coluna específica? (Digite o nome da coluna ou pressione Enter para continuar): ")
        condicao = input(
            "Deseja adicionar uma condição para filtrar os dados? (ex: '%substring%')\nDigite a condição ou pressione Enter para continuar sem filtro: ").lower()


        resultados = substring(conexao, tabela, nome_coluna if nome_coluna else None, condicao if condicao else None)


        if resultados:
            print(f"Dados encontrados: {resultados}")
        else:
            print("Nenhum dado encontrado na tabela com essa condição.")

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ou buscar dados no banco de dados: {err}")
    finally:
        conexao.close()


def atualizar_registro(conexao):
    tabelas_update = ["Cliente", "Filial", "Produto", "Vendedor", "Pagamento", "Desconto", "Pix", "Cartao", "ItemVenda",
                      "Gerente"]

    print("\nTabelas disponíveis:")
    for i in tabelas_update:
        print(f"- {i}")

    tabela_update = input("Digite o nome da tabela onde deseja atualizar o registro: ").strip()
    if tabela_update not in tabelas_update:
        print("Tabela inválida! Escolha uma tabela da lista.")
        return

    coluna_update = input("Digite o nome da coluna onde está localizado o registro a ser atualizado:").strip()
    novo_valor_update = input("Digite o novo valor do registro: ").strip()
    condição_update = input("Digite a condição em SQL:(Ex: salario > 2000)")

    query = f"""
        UPDATE {tabela_update}
        SET {coluna_update} = '{novo_valor_update}'
        WHERE {condição_update};
    """

    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        conexao.commit()
        print("Registro atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar o registro: {e}")
    finally:
        cursor.close()


def criar_gatilho_atualizar_salario_vendedor(conexao):
    cursor = conexao.cursor()
    try:

        cursor.execute("DROP TRIGGER IF EXISTS atualizar_salario_vendedor")

        cursor.execute("""
            DELIMITER $$

            CREATE TRIGGER atualizar_salario_vendedor
            AFTER INSERT ON Item_Venda
            FOR EACH ROW
            BEGIN
                DECLARE comissao DECIMAL(10,2);

                -- Calcula a comissão com base no preço do produto e quantidade vendida
                SELECT Preco * NEW.Quantidade * 0.05 
                INTO comissao
                FROM Produto
                WHERE NomeProduto = NEW.NomeProduto;

                -- Atualiza o salário do vendedor
                UPDATE Vendedor
                SET Salario = Salario + comissao
                WHERE ID_Vendedor = NEW.ID_Vendedor;
            END $$

            DELIMITER ;
        """)
        conexao.commit()
        print("Gatilho 'atualizar_salario_vendedor' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar gatilho: {e}")
    finally:
        cursor.close()


def produtos_preco_maior_que_todos_os_preco(conexao):
    # Consulta utilizando ALL

    e = input("digite o id filial para a clausula").lower()
    cursor = conexao.cursor()

    query = f"""
    SELECT p.NomeProduto, p.Preco
    FROM Produto p
    WHERE p.Preco >= ALL (SELECT f.Preco 
                         FROM Produto f 
                         WHERE f.ID_Filial = {e})
    """

    cursor.execute(query)
    resultado = cursor.fetchall()

    for produto in resultado:
        print(produto)

    cursor.close()


def vendedores_com_vendas_superiores_a_precos_filial_id(conexao):
    # Busca usando ANY
    e = input("digite o id filial para a clausula").lower()
    cursor = conexao.cursor()

    query = f"""
    SELECT v.Nome, iv.NomeProduto, iv.Quantidade
    FROM Vendedor v
    JOIN Item_Venda iv ON v.ID_Vendedor = iv.ID_Vendedor
    JOIN Produto p ON iv.NomeProduto = p.NomeProduto
    WHERE p.Preco > ANY (SELECT f.Preco 
                          FROM Produto f 
                          WHERE f.ID_Filial = {e} )
    """

    cursor.execute(query)
    resultado = cursor.fetchall()
    for vendedor in resultado:
        print(vendedor)
    cursor.close()


def totalvendasvendedorcliente(conexao):
    print("exibindo o total de vendas por vendedor e clientes ")
    query = """SELECT 
               v.Nome AS Vendedor,
               c.Nome AS Cliente,
               SUM(iv.Quantidade) AS Total_Vendido
               FROM Item_Venda iv
               INNER JOIN Vendedor v ON iv.ID_Vendedor = v.ID_Vendedor
               LEFT JOIN Cliente c ON iv.ID_Cliente = c.ID_Cliente
               GROUP BY v.Nome, c.Nome
              ORDER BY Total_Vendido DESC;"""
    try:
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        for i in resultados:
            print(f"nome do vendedor : {i[0]} , nome do cliente : {i[1]} , numero de vendas : {i[2]} ")
    except Exception as e:
        print(e)
    finally:
        cursor.close()


def funcao_GPH(conexao, nome_coluna, agregacao, condicao, tabela, ordem):
    cursor = conexao.cursor()
    try:
        if(agregacao == "count"):
            if(ordem == "dec"):
                query = f"SELECT {nome_coluna},{agregacao}(*) FROM {tabela} GROUP BY {nome_coluna} HAVING {nome_coluna}{condicao} ORDER BY {nome_coluna} DESC"

            else:
                query = f"SELECT {nome_coluna},{agregacao}(*) FROM {tabela} GROUP BY {nome_coluna} HAVING {nome_coluna}{condicao} ORDER BY {nome_coluna}"
            print(query)

            cursor.execute(query)
            return cursor.fetchall()

    except Exception as e:
        print(f"Erro ao buscar dados da tabela {tabela}: {e}")

    finally:
        cursor.close()


def group_by_having(conexao):
    cursor = conexao.cursor()
    lista_tabelas = ["Cliente", "Filial", "Produto", "Vendedor", "pagamento", "Desconto", "Pix", "Cartao", "ItemVenda" , "Gerente"]

    for e in lista_tabelas:
        print(f"{e}")

    tabela = input("Digite o nome de uma das tabelas:\n").lower()
    nome_coluna = input("Digite a coluna que vai ser utilizada na função GROUP BY:").strip()
    agregacao = "count"
    condicao = input("digite condicao que vai ser utilizada pelo HAVING (>2000)").strip()
    ordem = input("Decida a ordem de seleção digitando dec(decrescente) ou cre(crescente):").strip().lower()

    resultado = funcao_GPH(conexao, nome_coluna, agregacao, condicao, tabela, ordem)

    print(f"Resultados obtidos:{resultado}")