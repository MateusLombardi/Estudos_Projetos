def divnumeros():
    divisao  = 0
    n1 = int(input("digite o primeiro número: "))
    n2 = int(input("digite o segundo número: "))
    if (n1 % n2 == 0):
        divisao = n1/n2
        print(f"É divisível, o resultado é {int(divisao)}")
    else:
        print("Não e divisível")
    return n1/n2

divisao = divnumeros()


