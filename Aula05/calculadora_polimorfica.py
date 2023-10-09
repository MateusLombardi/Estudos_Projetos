class Calculadora:
    def calcular(self, num1, num2, operacao):
        pass

class CalculadoraSimples(Calculadora):
    def calcular(self, num1, num2, operacao):
        if operacao == '+':
            return num1 + num2
        elif operacao == '-':
            return num1 - num2
        elif operacao == '*':
            return num1 * num2
        elif operacao == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Divisão por zero não é permitida."

# Função para realizar cálculos com a calculadora
def realizar_calculos(calculadora, num1, num2, operacao):
    return calculadora.calcular(num1, num2, operacao)

# Exemplo de uso
calculadora_simples = CalculadoraSimples()

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacoes = ['+', '-', '*', '/']

for operacao in operacoes:
    resultado_simples = realizar_calculos(calculadora_simples, num1, num2, operacao)

    print(f"Resultado da calculadora simples ({operacao}): {resultado_simples}")
