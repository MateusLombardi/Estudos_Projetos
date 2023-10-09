print("############ Votação################")

idade = int(input("Qual sua idade? "))

if (idade < 16):
    print("você não pode votar!")
elif (idade >= 16 and idade < 18):
    print("facultativo")
elif (idade >= 18 and idade < 65):
    print("É obrigatorio votar!")
