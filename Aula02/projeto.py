lista_fruta=["maçã","maçã","maçã","abacaxi","abacaxi","abacaxi","banana","banana"]
maca=0
abacaxi=0
banana=0 
soma=0
fruta = (str(input("digite o nome da fruta")))
# maca =lista_fruta.count("maçã")
# print(f"Tem {maca} maçãs")
# abacaxi =lista_fruta.count("abacaxi")
# print(f"Tem {abacaxi} abacaxi")
# banana =lista_fruta.count("banana")
# print(f"Tem {banana} banana")

# for i in lista_fruta:
#     if i == "maçã":
#         maca= maca +1
#     elif i == "abacaxi":
#        abacaxi= abacaxi +1
#     else:
#         banana = banana + 1
# print(f"Tem {maca} Maçãs, {abacaxi} abacaxis e {banana} bananas")

for i  in lista_fruta:
    if i == fruta:
        soma = soma +1
print(f"Tem {soma} {fruta}")



