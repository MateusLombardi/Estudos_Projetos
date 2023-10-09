print("######################## Bem vindo ao verificador de números do SENAI! #####################################")
print()
print()
print()
print()
print()
print()
print("############################################################################################################")

cont = "Sim"

while (cont == "Sim"):
    numero = int(input("digite um numero"))

# if (numero > 0):
#     print ("Esse Número é positivo")
# elif (numero < 0):
#     print("Esse número é negativo")
# else:
#     print("Esse número é zero")

    if (numero % 2 == 0):
        print ("Esse número é par")
    else:
        print("Esse número e impar")
    cont = str(input("Quer continuar? "))
