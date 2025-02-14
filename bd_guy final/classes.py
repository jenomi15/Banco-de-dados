import mysql.connector
import datetime

class Filial:
    def __init__(self, id_filial=None, localizacao="", nome=None, telefone=None, tempodeparceria=None):
        self.id_filial = id_filial
        self.localizacao = localizacao
        self.nome = nome
        self.telefone = telefone
        self.tempodeparceria = tempodeparceria or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO Filial (Localizacao, Nome, Telefone, Tempodeparceria) VALUES (%s, %s, %s, %s)",
                (self.localizacao, self.nome, self.telefone, self.tempodeparceria)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir filial: {e}")
        finally:
            cursor.close()


class Gerente:
    def __init__(self, id_gerente=None, nome="", telefone=None, tempoemgerencia=None, numerofunc=None):
        self.id_gerente = id_gerente
        self.nome = nome
        self.telefone = telefone
        self.tempoemgerencia = tempoemgerencia or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.numerofunc = numerofunc

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO Gerente (Nome, Telefone, Tempoemgerencia, Numerofunc) VALUES (%s, %s, %s, %s)",
                (self.nome, self.telefone, self.tempoemgerencia, self.numerofunc)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir gerente: {e}")
        finally:
            cursor.close()


class Vendedor:
    def __init__(self, id_vendedor=None, nome="", id_filial=None, id_gerente=None, datadeentrada=None, telefone=None, salario=None):
        self.id_vendedor = id_vendedor
        self.nome = nome
        self.id_filial = id_filial
        self.id_gerente = id_gerente
        self.datadeentrada = datadeentrada or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.telefone = telefone
        self.salario = salario

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO Vendedor (Nome, ID_Filial, ID_Gerente, Datadeentrada, Telefone, Salario) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.nome, self.id_filial, self.id_gerente, self.datadeentrada, self.telefone, self.salario)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir vendedor: {e}")
        finally:
            cursor.close()


class Produto:
    def __init__(self, id_produto=None, nome_produto="", preco=0.0, datadecriacao=None, tamanho=None , nicho =None):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.preco = preco
        self.datadecriacao = datadecriacao or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tamanho = tamanho
        self.nicho = nicho

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO Produto (NomeProduto, Preco, Tamanho, Datadecriacao, Nicho) VALUES (%s, %s, %s, %s, %s)",
                (self.nome_produto, self.preco, self.tamanho, self.datadecriacao, self.nicho)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
        finally:
            cursor.close()


class Cliente:
    def __init__(self, id_cliente=None, nome="", telefone=None, datadeentrada=None, endereco=None):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.datadeentrada = datadeentrada or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.endereco = endereco

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO Cliente (Nome, Telefone, Datadeentrada, Endereco) VALUES (%s, %s, %s, %s)",
                (self.nome, self.telefone, self.datadeentrada, self.endereco)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")
        finally:
            cursor.close()


class Pagamento:
    def __init__(self, id_pagamento=None, valor_total=0.0, id_cliente=None, banco=None, datapagamento=None, aprovado=None):
        self.id_pagamento = id_pagamento
        self.valor_total = valor_total
        self.id_cliente = id_cliente
        self.banco = banco
        self.datapagamento = datapagamento or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.aprovado = aprovado

    def inserir(self, conexao):
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO Pagamento (ValorTotal, ID_Cliente, Banco, Datapagamento, Aprovado) VALUES (%s, %s, %s, %s, %s)",
                (self.valor_total, self.id_cliente, self.banco, self.datapagamento, self.aprovado)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir pagamento: {e}")
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
            cursor.execute(
                "INSERT INTO Desconto (ID_Pagamento, ValorDesconto) VALUES (%s, %s)",
                (self.id_pagamento, self.valor_desconto)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir desconto: {e}")
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
            cursor.execute(
                "INSERT INTO Pix (ID_Pagamento, Banco) VALUES (%s, %s)",
                (self.id_pagamento, self.banco)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir Pix: {e}")
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
            cursor.execute(
                "INSERT INTO Cartao (ID_Pagamento, Parcelas) VALUES (%s, %s)",
                (self.id_pagamento, self.parcelas)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir cartão: {e}")
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
            cursor.execute(
                "INSERT INTO Item_Venda (NomeProduto, Quantidade, ID_Vendedor, ID_Cliente) VALUES (%s, %s, %s, %s)",
                (self.nome_produto, self.quantidade, self.id_vendedor, self.id_cliente)
            )
            conexao.commit()
        except Exception as e:
            print(f"Erro ao inserir item de venda: {e}")
        finally:
            cursor.close()