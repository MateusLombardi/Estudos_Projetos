hotel = {
    '106': {'tipo':'Solteiro', 'preco':1054, 'reserva': False},
    '100': {'tipo':'Solteiro', 'preco':120, 'reserva': False},
    '101': {'tipo':'Solteiro', 'preco':100, 'reserva': False},
    '102': {'tipo':'Solteiro', 'preco':150, 'reserva': False},
    '103': {'tipo':'Casal', 'preco':1090, 'reserva': True},
    '104': {'tipo':'Casal', 'preco':1001, 'reserva': True},
    '105': {'tipo':'Casal', 'preco':1002, 'reserva': True}     
}


def listar_quartos_disponiveis():
    print('Quartos disponíveis:')
    for numero, info in hotel.items():
        if info ['disponivel']:
            print(f'quarto {numero}: Tipo{info["tipo"]}, Preco R${info["preco"]} reservado {info["reserva"]}')

def adicionar_ou_remover_reserva(): 
   quarto = str(input("Digite o quarto: "))

   if quarto in hotel:
       hotel[quarto]["reserva"] = not hotel[quarto]["reserva"]
       
opcao = "S"
while opcao == "S":
    com = int(input("Para adicionar ou remover digite: [1] \nPara remover digite:   [2]"))
    
    if (com == 1):
        adicionar_ou_remover_reserva() 
    elif (com == 2):
        listar_quartos_disponiveis()
    else:
        print("Opção invalida")
    
    for hotel,  info in hotel.items():
        print("C/S".ljust(30), "preço".ljust(30), "reservado".ljust(30))
    opcao = str(input("deseja continuar?"))
    
