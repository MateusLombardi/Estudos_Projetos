class Pessoa:
    def __init__(self, nome, profissao, e_Civil, idade):
        self.nome=nome
        self.profissao=profissao
        self.e_Civil=e_Civil
        self.idade=idade
    
    def imprimir_pessoa(self):
        print("Nome: ", self.nome)
        print("Profissão: ", self.profissao)
        print("Estado Civil: ", self.e_Civil)
        print("Idade: ", self.idade)

class Aluno(Pessoa):
    def __init__(self,aluno, curso, nome, profissao, e_Civil, idade):
        super().__init__(nome, profissao, e_Civil, idade)
        self.aluno= aluno
        self.curso= curso

    

aluno= Aluno("Mateus","Python","Lombardi","Eletricista","Solteiro",23)

aluno.imprimir_pessoa()










        
        