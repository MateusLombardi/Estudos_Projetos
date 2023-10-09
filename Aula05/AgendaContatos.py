class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def apresentar(self):
        pass

class ContatoPessoal(Contato):
    def __init__(self, nome, telefone, endereco):
        super().__init__(nome, telefone)
        self.endereco = endereco

    def apresentar(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"

class ContatoProfissional(Contato):
    def __init__(self, nome, telefone, empresa):
        super().__init__(nome, telefone)
        self.empresa = empresa

    def apresentar(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEmpresa: {self.empresa}"

# Função para listar os contatos
def listar_contatos(agenda):
    for contato in agenda:
        print(contato.apresentar())
        print('-' * 30)

# Exemplo de uso
agenda = []

contato1 = ContatoPessoal("João", "123-456-7890", "Rua A, Cidade X")
contato2 = ContatoProfissional("Maria", "987-654-3210", "Empresa Y")
contato3 = ContatoPessoal("Carlos", "555-123-4567", "Rua B, Cidade Z")

agenda.append(contato1)
agenda.append(contato2)
agenda.append(contato3)

listar_contatos(agenda)
