tarefa={}


def opcao():
    print("escolha uma opção abaixo para continuar com sua agenda de tarefas")
    print("para adicionar uma nova tarefa digite [1]")
    print("para remover uma tarefa digite [2]")
    print("para editar uma tarefa digite [3]")
    print("para visualizar as tarefas digite [4]")
    print("se deseja encerrar digite [5]")

    
    
def adicionar_tarefa():
    data=str(input("digite a data"))
    hora=str(input("digite a hora"))
    assunto=str(input("digite o assunto?"))
    tarefa[data] = hora
    tarefa[data] = assunto
    print("Tarefa adicionada com sucesso!")

def remover_tarefa():
    data= str(input("Digite a tarefa que deseja remover:"))
    if data == data:
        del tarefa[data]
        print("tarefa removida com sucesso!")
    else:
        print("A tarefa está vazia")

def atualizar_tarefas():
    data = str(input("Digite o nome: "))
    if  data == data in tarefa:
        hora = str(input("Digite o  novo horário: "))
        tarefa[data] = hora
        assunto = str(input("Digite o  novo assunto: "))
        tarefa[data] = assunto
    else:
        print("Tarefa não encontrada!")

def visualizar_tarefa():
    print(tarefa)
        
def escolha():
    continuar = "S"
    com = 0
    
    while continuar == "S":
        opcao()
        com = int(input("Digite o numero da opção:"))
        if (com == 1):
            adicionar_tarefa()
        elif (com == 2):
            remover_tarefa()
        elif (com == 3):
            atualizar_tarefas()
        elif (com == 4):
            visualizar_tarefa()
        elif (com == 5):
            continuar = "N"
            print("programa encerrado com sucesso!")
        else:
            print("Opção invalida")

escolha()

