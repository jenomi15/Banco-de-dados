import mysql.connector
from classes import Cliente, Filial, Produto, Vendedor, Gerente, Pagamento, Desconto, Pix, Cartao, ItemVenda
from funcoes import EMmassa
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
    janela = tk.Tk()
    janela.title("Aplicativo Banco de Dados")
    janela.geometry("400x300")
    label = tk.Label(janela, text="Olá, bem-vindo ao sistema da Loja Guy", font=("Arial", 16))
    label.pack(pady=20)
    botao = tk.Button(janela, text="Clique aqui", command=lambda: EMmassa(conexao, tabelas))
    botao.pack(pady=10)

    
    janela.mainloop()

main()