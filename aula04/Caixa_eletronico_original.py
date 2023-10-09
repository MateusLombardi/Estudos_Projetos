from def_Caixa import Conta
        
lista_contas=[]
lista_contas.append(Conta("Mateus","55585458",1000,6000,"123"))
lista_contas.append(Conta("Mateus 1","54548458",1000,6000,"1234"))
lista_contas.append(Conta("Mateus 2","8821215458",8000,9000,"12345"))
lista_contas.append(Conta("Mateus 3","955585458",1000,6000,"123456"))
lista_contas.append(Conta("Mateus 4","155585458",1000,6000,"1234567"))



nome_V=str(input("Digite o seu nome: "))
cpf_V=str(input("Digite o seu cpf: "))
senha_V=str(input("Digite a senha: "))
conta_Logada={}

for conta in lista_contas:
    if conta.nome == nome_V and conta.cpf == cpf_V and conta.senha == senha_V:
       conta_Logada= conta
       print(f"Bem vindo {conta.nome}!")
       print(f"Seu saldo é de {conta.saldo}")
       print(f"Seu limite é de {conta.limit}")
       print("se deseja efetuar um deposito digite[1]")
       print("se deseja efetuar um saque digite [2]") 
       print("para sair digite [3]")
       break
opcao=0

while opcao != 3:
    opcao= int(input("qual ação deseja efetuar? "))
    if opcao == 1:
        valor_deposito = int(input("digite o valor de deposito "))
        conta_Logada.deposito(valor_deposito)
        print(f"Seu saldo e de {conta_Logada.saldo}")
    elif opcao == 2:
        valor_saque = int(input("digite o valor de saque "))
        conta_Logada.saque(valor_saque)
        print(f"Seu saldo e de ({conta_Logada.saldo})")

print("VOLTE SEMPRE!")