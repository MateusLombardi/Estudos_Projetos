def verifica_idada():
    idade= int(input("digite a sua idade"))
    
    if (idade < 16):
        print("Você não pode assistir ao filme:")
    elif(idade >= 16):
        print("Você pode assistir ao filme.")

verifica_idada()