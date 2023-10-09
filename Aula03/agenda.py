contatos={}
lista=[]
def adicionar_contatos():
    nome = str(input("Digite o nome: "))
    numero = str(input("Digite o numero: "))
    contatos[nome]=numero
    
def remover_contatos():
    nome = str(input("Digite o nome: "))
    if  nome == nome in contatos:
        del contatos[nome]
    else:
        print("nome não encontrado!")

def atualizar_contatos():
    nome = str(input("Digite o nome: "))
    if  nome == nome in contatos:
        numero = str(input("Digite o numero: "))
        contatos[nome] = numero
    else:
        print("nome não encontrado!")
   
opcao = "S"
while opcao == "S":
    com = int(input("Para adicionar digite: [1] \nPara remover digite:   [2]\nPara atualizar digite: [3]"))
    print(contatos)
    if (com == 1):
        adicionar_contatos()
    elif (com == 2):
        remover_contatos()
    elif (com == 3):
        atualizar_contatos()
    else:
        print("Opção invalida")
    
    for nome,  numero in contatos.items():
        print("Nome".ljust(30), "Numero".ljust(30))
        print( )
        print(str(nome).ljust(30), str(numero).ljust(30))
    opcao = str(input("deseja continuar?"))
    
