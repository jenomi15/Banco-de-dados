import mysql.connector
from classes import Cliente, Filial, Produto, Vendedor, Gerente, Pagamento, Desconto, Pix, Cartao, ItemVenda 
from funcoes import EMmassa , buscar ,busca_do_usuario , busca_geral
import tkinter as tk
from tkinterface import botao_capturar , botao_clicado
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

   
    janela = tk.Tk()
    janela.title("Aplicativo Banco de Dados")
    janela.geometry("400x300")
    label = tk.Label(janela, text="Olá, bem-vindo ao sistema da Loja Guy", font=("Arial", 16))
    label.grid(row=0, column=0, pady=20)  
    botao_massa = tk.Button(janela, text="Clique aqui para executar o em massa", command=lambda: EMmassa(conexao))
    botao_busca = tk.Button(janela, text="Clique aqui para executar a busca", command=lambda: buscar(conexao))
    botao_massa.grid(row=1, column=0, padx=10, pady=10)
    botao_busca.grid(row=2, column=0, padx=10, pady=10)

    
    janela.mainloop()
    buscar(conexao)
    busca_do_usuario(conexao)
    


main()  