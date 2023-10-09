print("/////////////////// SEJA BEM VINDO ////////////////")
p= "S"
Lista = ["celular"]
print(Lista)
#Adicionar item na lista
def Additem():
    # add = str(input("digite o nome do produto: "))
    Lista.append(str(input("digite o nome do produto: ")))
    

def removeritem():
    Lista.remove(str(input("digite o item que deseja remover: ")))

def exibiritem():
    print(Lista)

while p == "S":
    com = int(input("Para adicionar digite [1]/////// Para remover digite [2]///// Para exibir digite[3]"))
    if (com == 1):
        Additem()
    elif (com == 2):
        removeritem()
    elif (com == 3):
        exibiritem()
    else:
        print("Opção invalida")
    print(Lista)
    