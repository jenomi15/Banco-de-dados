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
        inserir(y, conexao)
