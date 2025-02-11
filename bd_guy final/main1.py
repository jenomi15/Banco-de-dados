import mysql.connector
from classes import Cliente, Filial, Produto, Vendedor, Gerente, Pagamento, Desconto, Pix, Cartao, ItemVenda 
from funcoes import EMmassa , buscar ,busca_do_usuario , busca_geral , deletar , insere , VendasPorFilial , totalvendasvendedorcliente

#senha = (str(input("digite a senha")))
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password= "Mestrepokemon2006#" ,
    database="loja_guy"
)
#cursor = conexao.cursor()
#tabela = (str(input("digite a tabela")))
#query = f"SELECT * FROM `{tabela}`"
#cursor.execute(query)
#meuresultado = cursor.fetchall()
#for i in meuresultado:
    #print(i)
#nome = input("Digite o nome do cliente: ").strip()
#insert_query = "INSERT INTO Cliente (Nome) VALUES (%s)"
#cursor.execute(insert_query, (nome,))  
#conexao.commit()  
#cursor.close()
#conexao.close()  
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
}
    

def main():
   
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Mestrepokemon2006#",
        database="loja_guy"
    )
    #totalvendasvendedorcliente(conexao)
    #VendasPorFilial(conexao)
    #insere(conexao)
    #deletar(conexao)
    #EMmassa(conexao)
    #buscar(conexao)
    busca_do_usuario(conexao)
    


main()  