class Conta:
    nome: str
    saldo:float
    cpf:str
    limit:float
    senha:str


    def __init__(self, nome, cpf, saldo, limit, senha, investimento):
        self.nome=nome
        self.cpf=cpf
        self.saldo=saldo
        self.limit=limit
        self.senha = senha
        self.investimento= investimento

    def Saldo_def(self):
        print(self.saldo)

    def deposito(self,valor_deposito):
        self.saldo = self.saldo + valor_deposito
        return self.saldo

    def saque(self,valor_saque):
        self.saldo = self.saldo- valor_saque
        return  self.saldo

    def login(self, nome, cpf, senha, saldo, limit):
        if self.nome == nome and self.cpf == cpf and self.senha == senha:
            print(f"Bem vindo {nome}!")
            print(f"Seu saldo é de {saldo}")
            print(f"Seu limite é de {limit}")
        else:
            print("Nome,CPF e Senha incorretos!")

        



