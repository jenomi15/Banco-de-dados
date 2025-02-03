import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password= "Mestrepokemon2006#" ,
    database="loja_guy"
)
def EMmassa(conexao, tabelas):
    
    if not conexao.is_connected():
        print("fazendo a conexao")
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Mestrepokemon2006#",
            database="loja_guy"
        )

    print("\nTabelas disponíveis:")
    for j, tabela in enumerate(tabelas.keys(), start=1):
        print(f"{j}. {tabela}")

    tabeladesejada = input("\nDigite a tabela desejada: ").strip()
    while tabeladesejada not in tabelas:
        tabeladesejada = input("Essa tabela não está presente. Digite novamente: ").strip()
    classe_escolhida = tabelas[tabeladesejada]

    quantidade = int(input("Quantos registros você deseja inserir? ").strip())
    lista_objetos = []
    for _ in range(quantidade):
        if tabeladesejada == "Cliente":
            nome = input("Digite o nome do cliente: ").strip()
            objeto = classe_escolhida(nome=nome)
        
        elif tabeladesejada == "Filial":
            localizacao = input("Digite a localização da filial: ").strip()
            objeto = classe_escolhida(localizacao=localizacao)

        elif tabeladesejada == "Produto":
            nome_produto = input("Digite o nome do produto: ").strip()
            preco = float(input("Digite o preço do produto: ").strip())
            objeto = classe_escolhida(nome_produto=nome_produto, preco=preco)

        elif tabeladesejada == "Vendedor":
            nome_vendedor = input("Digite o nome do vendedor: ").strip()
            id_filial = int(input("Digite o ID da filial: ").strip())
            id_gerente = int(input("Digite o ID do gerente: ").strip())
            objeto = classe_escolhida(nome=nome_vendedor, id_filial=id_filial, id_gerente=id_gerente)

        elif tabeladesejada == "Pagamento":
            valor_total = float(input("Digite o valor total do pagamento: ").strip())
            id_cliente = int(input("Digite o ID do cliente: ").strip())
            objeto = classe_escolhida(valor_total=valor_total, id_cliente=id_cliente)

        elif tabeladesejada == "Desconto":
            valor_desconto = float(input("Digite o valor do desconto: ").strip())
            id_pagamento = int(input("Digite o ID do pagamento: ").strip())
            objeto = classe_escolhida(valor_desconto=valor_desconto, id_pagamento=id_pagamento)

        elif tabeladesejada == "Pix":
            banco = input("Digite o banco do pagamento: ").strip()
            id_pagamento = int(input("Digite o ID do pagamento: ").strip())
            objeto = classe_escolhida(banco=banco, id_pagamento=id_pagamento)

        elif tabeladesejada == "Cartao":
            parcelas = int(input("Digite o número de parcelas: ").strip())
            id_pagamento = int(input("Digite o ID do pagamento: ").strip())
            objeto = classe_escolhida(parcelas=parcelas, id_pagamento=id_pagamento)

        elif tabeladesejada == "ItemVenda":
            nome_produto = input("Digite o nome do produto: ").strip()
            quantidade = int(input("Digite a quantidade: ").strip())
            id_vendedor = int(input("Digite o ID do vendedor: ").strip())
            id_cliente = int(input("Digite o ID do cliente: ").strip())
            objeto = classe_escolhida(nome_produto=nome_produto, quantidade=quantidade, id_vendedor=id_vendedor, id_cliente=id_cliente)

        lista_objetos.append(objeto)

    for objeto in lista_objetos:
        objeto.inserir(conexao)

    print(f"{quantidade} registros inseridos com sucesso!")