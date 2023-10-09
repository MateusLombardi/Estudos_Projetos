import mysql.connector

# Função para criar a conexão com o MySQL
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="seu_usuario",
            password="sua_senha",
            database="seu_banco_de_dados"
        )
        return conexao
    except mysql.connector.Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return None

# Função para inserir um produto
def inserir_produto(conexao, nome, quantidade, valor):
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Produto (Nome, quantidade, valor) VALUES (%s, %s, %s)"
        val = (nome, quantidade, valor)
        cursor.execute(sql, val)
        conexao.commit()
        print("Produto inserido com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao inserir produto:", err)
    finally:
        cursor.close()

# Função para inserir um cliente
def inserir_cliente(conexao, nome, contato):
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Cliente (nome, contato) VALUES (%s, %s)"
        val = (nome, contato)
        cursor.execute(sql, val)
        conexao.commit()
        print("Cliente inserido com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao inserir cliente:", err)
    finally:
        cursor.close()

# Função para registrar uma compra
def registrar_compra(conexao, id_produto, id_cliente, quantidade, valor):
    cursor = conexao.cursor()
    try:
        sql = "INSERT INTO Compras (idProduto, idCliente, quantidade, valor) VALUES (%s, %s, %s, %s)"
        val = (id_produto, id_cliente, quantidade, valor)
        cursor.execute(sql, val)
        conexao.commit()
        print("Compra registrada com sucesso!")
    except mysql.connector.Error as err:
        print("Erro ao registrar compra:", err)
    finally:
        cursor.close()

# Função principal
def main():
    conexao = conectar()
    if conexao:
        while True:
            print("\nEscolha uma opção:")
            print("1. Inserir Produto")
            print("2. Inserir Cliente")
            print("3. Registrar Compra")
            print("4. Sair")
            
            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                nome = input("Digite o nome do produto: ")
                quantidade = input("Digite a quantidade: ")
                valor = input("Digite o valor: ")
                inserir_produto(conexao, nome, quantidade, valor)
            elif opcao == "2":
                nome = input("Digite o nome do cliente: ")
                contato = input("Digite o contato: ")
                inserir_cliente(conexao, nome, contato)
            elif opcao == "3":
                id_produto = input("Digite o ID do produto: ")
                id_cliente = input("Digite o ID do cliente: ")
                quantidade = input("Digite a quantidade: ")
                valor = input("Digite o valor: ")
                registrar_compra(conexao, id_produto, id_cliente, quantidade, valor)
            elif opcao == "4":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        conexao.close()

if __name__ == "__main__":
    main()
