# self={'nome': "Mateus", "saldo": 0, "CPF":5158854585, "Limite":9999}
# def saldo():
#     print(self["Saldo"])

# def deposito(valor_deposito):
#     self["saldo"] = self["saldo"]+ valor_deposito
#     return self["saldo"]

# def saque(valor_saque):
#     self["saldo"] = self["saldo"]- valor_saque
#     return  self["saldo"]

# valor_deposito=0
# valor_saque=0

class Conta:
    nome: str

    def __init__(self, nome, cpf, saldo, limit):
        self.nome=nome
        self.cpf=cpf
        self.saldo=saldo
        self.limit=limit

    def Saldo_def(self):
        print(self.saldo)

    def deposito(self,valor_deposito):
        self.saldo = self.saldo + valor_deposito
        return self.saldo

    def saque(self,valor_saque):
        self.saldo = self.saldo- valor_saque
        return  self.saldo




# lista_contas = []

# lista_contas.append(Conta("Mateus","55585458",1000,6000))
# lista_contas.append(Conta("Mateus 1","55585458",1000,6000))
# lista_contas.append(Conta("Mateus 2","55585458",8000,9000))
# lista_contas.append(Conta("Mateus 3","55585458",1000,6000))
# lista_contas.append(Conta("Mateus 4","55585458",1000,6000))

# for conta in lista_contas:
#     if conta.nome == "Mateus 2":
#         print(conta.saldo)




