
import mysql.connector

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

# Função para criar a conexão com o MySQL
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="senai",
            database="agenda"
        )
        return conexao
    except mysql.connector.Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return None
    
# Função para inserir contato
def inserir_contato(conexao, nome, numero, endereco):
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO contatos (nome, numero, endereco) VALUES (%s, %s, %s)"
        
        val = (nome, numero, endereco)
        cursor.execute(sql, val)
        conexao.commit()
        print("Dados inseridos com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao inserir produto:", err)
    finally:
        cursor.close()


nome= input("Digite o nome do contato: ")
numero = int(input("Digie o telefone de contato sem traços: "))
endereco = input("Digite o nome da rua do contato: ")

conexao = conectar()
inserir_contato( conexao, nome, numero, endereco )
# agenda = []

# contato1 = ContatoPessoal("João", "123-456-7890", "Rua A, Cidade X")
# contato2 = ContatoProfissional("Maria", "987-654-3210", "Empresa Y")
# contato3 = ContatoPessoal("Carlos", "555-123-4567", "Rua B, Cidade Z")

#inserir_produto()

# agenda.append(contato1)
# agenda.append(contato2)
# agenda.append(contato3)

# listar_contatos(agenda)
