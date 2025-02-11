import mysql.connector

class Filial:
    def __init__(self, id_filial=None, localizacao=""):
        self.id_filial = id_filial
        self.localizacao = localizacao

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Filial (Localizacao) VALUES (%s)", (self.localizacao,))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir a filial: {e}")
        finally:
            cursor.close()
   


class Gerente:
    def __init__(self, id_gerente=None, nome=""):
        self.id_gerente = id_gerente
        self.nome = nome

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Gerente (Nome) VALUES (%s)", (self.nome,))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir o gerente: {e}")
        finally:
            cursor.close()

class Vendedor:
    def __init__(self, id_vendedor=None, nome="", id_filial=None, id_gerente=None):
        self.id_vendedor = id_vendedor
        self.nome = nome
        self.id_filial = id_filial
        self.id_gerente = id_gerente

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Vendedor (Nome, ID_Filial, ID_Gerente) VALUES (%s, %s, %s)",
                           (self.nome, self.id_filial, self.id_gerente))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir o vendedor: {e}")
        finally:
            cursor.close()

class Produto:
    def __init__(self, id_produto=None, nome_produto="", preco=0.0):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.preco = preco

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Produto (NomeProduto, Preco) VALUES (%s, %s)",
                           (self.nome_produto, self.preco))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir o  produto: {e}")
        finally:
            cursor.close()

class Cliente:
    def __init__(self, id_cliente=None, nome=""):
        self.id_cliente = id_cliente
        self.nome = nome

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Cliente (Nome) VALUES (%s)", (self.nome,))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir o  cliente: {e}")
        finally:
            cursor.close()

class Pagamento:
    def __init__(self, id_pagamento=None, valor_total=0.0, id_cliente=None):
        self.id_pagamento = id_pagamento
        self.valor_total = valor_total
        self.id_cliente = id_cliente

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Pagamento (ValorTotal, ID_Cliente) VALUES (%s, %s)",
                           (self.valor_total, self.id_cliente))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir o  pagamento: {e}")
        finally:
            cursor.close()

class Desconto:
    def __init__(self, id_desconto=None, id_pagamento=None, valor_desconto=0.0):
        self.id_desconto = id_desconto
        self.id_pagamento = id_pagamento
        self.valor_desconto = valor_desconto

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Desconto (ID_Pagamento, ValorDesconto) VALUES (%s, %s)",
                           (self.id_pagamento, self.valor_desconto))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir o desconto: {e}")
        finally:
            cursor.close()

class Pix:
    def __init__(self, id_pix=None, id_pagamento=None, banco=""):
        self.id_pix = id_pix
        self.id_pagamento = id_pagamento
        self.banco = banco

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Pix (ID_Pagamento, Banco) VALUES (%s, %s)",
                           (self.id_pagamento, self.banco))
            conexao.commit()
        except Exception as e:
            print(f"vacilo ao inserir o pagamento via Pix: {e}")
        finally:
            cursor.close()

class Cartao:
    def __init__(self, id_cartao=None, id_pagamento=None, parcelas=1):
        self.id_cartao = id_cartao
        self.id_pagamento = id_pagamento
        self.parcelas = parcelas

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Cartao (ID_Pagamento, Parcelas) VALUES (%s, %s)",
                           (self.id_pagamento, self.parcelas))
            conexao.commit()
        except Exception as e:
            print(f"vacilo o inseri o  pagamento via cartão: {e}")
        finally:
            cursor.close()

class ItemVenda:
    def __init__(self, id_item=None, nome_produto="", quantidade=1, id_vendedor=None, id_cliente=None):
        self.id_item = id_item
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.id_vendedor = id_vendedor
        self.id_cliente = id_cliente

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute("INSERT INTO Item_Venda (NomeProduto, Quantidade, ID_Vendedor, ID_Cliente) VALUES (%s, %s, %s, %s)",
                           (self.nome_produto, self.quantidade, self.id_vendedor, self.id_cliente))
            conexao.commit()
            print("Item de venda inserido com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir item de venda: {e}")
        finally:
            cursor.close()
   