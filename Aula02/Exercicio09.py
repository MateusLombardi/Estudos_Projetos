# lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in lista_numero:
#     if (i % 2 == 0):
#         print(i)
# print("Esses são os numeros pares")

# minha_lista=[]

# Numero = (int(input("digite um número")))
# resultado = 0
# for i in range(11):
#     resultado = Numero*i
#     print(Numero, "X",i, "=",resultado)

# numero = 0
# for i in range(101):
#     if i % 2 == 0:
#         numero = i + numero
# print(numero)

numero = (int(input("digite um número:")))
fatorial = 1
for numero in range(1, numero+1):
   fatorial = numero*fatorial

print(fatorial)

print(f"O fatorial é {fatorial}")