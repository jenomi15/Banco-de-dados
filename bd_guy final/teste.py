import tkinter as tk

def mostrar_frame(frame):
    """Esconde todos os frames e exibe apenas o frame desejado"""
    frame_inicial.pack_forget()
    frame_em_massa.pack_forget()

    frame.pack(fill="both", expand=True)

# Criando a janela principal
janela = tk.Tk()
janela.title("Sistema de Abas")

# ====== Criando o Frame Inicial ======
frame_inicial = tk.Frame(janela)
frame_inicial.pack(fill="both", expand=True)

titulo_inicial = tk.Label(frame_inicial, text="Tela Inicial", font=("Arial", 16))
titulo_inicial.pack(pady=20)

botao_ir_para_em_massa = tk.Button(frame_inicial, text="Ir para EMmassa", command=lambda: mostrar_frame(frame_em_massa))
botao_ir_para_em_massa.pack(pady=10)

# ====== Criando o Frame EMmassa ======
frame_em_massa = tk.Frame(janela)

titulo_em_massa = tk.Label(frame_em_massa, text="EMmassa em execução", font=("Arial", 16))
titulo_em_massa.pack(pady=20)

botao_voltar = tk.Button(frame_em_massa, text="Voltar", command=lambda: mostrar_frame(frame_inicial))
botao_voltar.pack(pady=10)

# Iniciando na tela inicial
mostrar_frame(frame_inicial)

# Iniciar loop da interface
janela.mainloop()
