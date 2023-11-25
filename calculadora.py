import tkinter as tk

n1=3
n2=3
soma=0



def multiplicar():
     soma = n1*n2

def somar():
     soma = n1+n2

def dividir():
    soma = n1 / n2 


def subtrair():
     soma = n1-n2 

janela = tk.Tk()
janela.title("Calculadora")

rotulo=tk.Label(janela,text="Insira os numeros em que deseja efetuar a operação")
rotulo.pack()



bt_soma=tk.Button(janela, text="+",command= somar()) 
bt_soma.pack()

bt_subtrair=tk.Button(janela, text="-",command= subtrair()) 
bt_subtrair.pack()


bt_multiplicar=tk.Button(janela, text="*",command= multiplicar()) 
bt_multiplicar.pack()

bt_div=tk.Button(janela, text="/",command= dividir()) 
bt_div.pack()


# #entrada de números
# entrada1=tk.Entry(janela)
# entrada2=tk.Entry(janela)

# #Botão que efetua uma operação
# def efetua_soma():
#      valor1_str = float(entrada1.get())
#      valor2_str = float
#      resultado = valor1_str +

bt_1=tk.Button(janela, text="1") 
bt_1.pack()

bt_2=tk.Button(janela, text="2") 
bt_2.pack()

bt_3=tk.Button(janela, text="3") 
bt_3.pack()

bt_4=tk.Button(janela, text="4") 
bt_4.pack()

bt_5=tk.Button(janela, text="5") 
bt_5.pack()

bt_6=tk.Button(janela, text="6") 
bt_6.pack()

bt_7=tk.Button(janela, text="7") 
bt_7.pack()

bt_8=tk.Button(janela, text="8") 
bt_8.pack()

bt_9=tk.Button(janela, text="9") 
bt_9.pack()

bt_0=tk.Button(janela, text="0") 
bt_0.pack()

#chamando o método de execução
janela.mainloop()

