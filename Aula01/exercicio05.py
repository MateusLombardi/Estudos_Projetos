numero1 = int(input("Digite o primeiro número "))
numero2 = int(input("Digite o segundo  número "))
numero3 = int(input("Digite o terceiro número "))

if (numero1 == numero2 and numero3 == numero1):
    print("E um triangulo equilatero")
elif (numero1 != numero2 and numero3 != numero1 and numero2 != numero3):
    print("É um triangulo escaleno")
else:
    print("É um triangulo isoceles")