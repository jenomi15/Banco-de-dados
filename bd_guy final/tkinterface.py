import tkinter as tk

# Função que será chamada quando o botão for clicado
def botao_clicado():
    print("Botão clicado!")

# Função para capturar o texto da caixa de texto
def capturar_texto():
    texto = caixa_texto.get()
    print(f"Texto digitado: {texto}")



def botao_capturar(caixa_texto):
    texto = caixa_texto.get()
    print(f"Texto digitado: {texto}")