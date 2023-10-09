import sqlite3

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

# Função para criar uma tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            tipo TEXT,
            endereco TEXT,
            empresa TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um novo contato ao banco de dados
def adicionar_contato(contato):
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()

    if isinstance(contato, ContatoPessoal):
        cursor.execute('''
            INSERT INTO contatos (nome, telefone, tipo, endereco)
            VALUES (?, ?, ?, ?)
        ''', (contato.nome, contato.telefone, 'pessoal', contato.endereco))
    elif isinstance(contato, ContatoProfissional):
        cursor.execute('''
            INSERT INTO contatos (nome, telefone, tipo, empresa)
            VALUES (?, ?, ?, ?)
        ''', (contato.nome, contato.telefone, 'profissional', contato.empresa))

    conn.commit()
    conn.close()

# Função para recuperar contatos do banco de dados
def recuperar_contatos():
    conn = sqlite3.connect('agenda.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contatos')
    contatos = []

    for row in cursor.fetchall():
        if row[3] == 'pessoal':
            contatos.append(ContatoPessoal(row[1], row[2], row[4]))
        elif row[3] == 'profissional':
            contatos.append(ContatoProfissional(row[1], row[2], row[5]))

    conn.close()
    return contatos

# Criar a tabela no banco de dados
criar_tabela()

# Exemplo de uso
contato1 = ContatoPessoal("João", "123-456-7890", "Rua A, Cidade X")
contato2 = ContatoProfissional("Maria", "987-654-3210", "Empresa Y")
contato3 = ContatoPessoal("Carlos", "555-123-4567", "Rua B, Cidade Z")

adicionar_contato(contato1)
adicionar_contato(contato2)
adicionar_contato(contato3)

agenda = recuperar_contatos()
listar_contatos(agenda)
