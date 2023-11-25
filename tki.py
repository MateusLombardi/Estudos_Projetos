import tkinter as tk
def mensagem():
    print("você clicou no botão")

janela = tk.Tk()
janela.title("Minha primeira interface com tkinter")

rotulo = tk.Label(janela, text = "Nome")

#Adicionando o rótulo a janela
rotulo.pack()

#Criando um botão
btn_clicar= tk.Button(janela, text = "Clique em mim", command= mensagem())
btn_clicar.pack()


#Entry (Entrada de Texto)

entrada= tk.Entry(janela)
entrada.pack()

#Fiel/Text (Área de Texto)
area_de_texto = tk.Text(janela)
area_de_texto.pack()

#Frame (Quadro)
frame = tk.Frame(janela)
frame.pack()

# Checkbutton (Botão de seleção)
check = tk.Checkbutton(janela,text="Opção 1")
check2= tk.Checkbutton(janela,text="Opção 2")
check.pack()
check2.pack()
 
#Radionbutton ( Botão de seleção redondo)

radion1 = tk.Radiobutton(janela,text="Opção 1", value=1)
radion2 = tk.Radiobutton(janela,text="Opção 2", value=2)
radion1.pack()
radion2.pack()

#Adicionando uma lista (Caixa de Listagem)
lista=tk.Listbox(janela)
lista.insert(1,"São Paulo")
lista.insert(2,"Rio de Janeiro")
lista.insert(3,"Amazonas")
lista.pack()




#chamando o método de execução
janela.mainloop()

