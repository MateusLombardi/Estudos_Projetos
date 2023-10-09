numero = int(input("Digite um número "))
Mult = int(input("Digite o número multiplo "))

if (numero % Mult == 0):
    print(numero," É multiplo de ", Mult)
else:
    print(numero, " Não é multiplo de ", Mult)