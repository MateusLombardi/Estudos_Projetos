import tkinter as tk
from tkinter import PhotoImage

def exibir_imagem():
    imagem = PhotoImage(file=".\img\goku.jpg")
    rotulo_imagem.config(imagem=imagem)

#Criando nossa Janela

janela= tk.Tk()
janela.title("inserindo Imagens")
#Janela.geometry (500 x 500, 200 , 200)

botao_carregar_imagem= tk.Button(janela,text="Carregar Imagem", command = exibir_imagem)
botao_carregar_imagem.pack(pady = 10)

#Criando um rótulo para a imagem
rotulo_imagem = tk.Label(janela)
rotulo_imagem.pack(pady=10)

janela.mainloop()
