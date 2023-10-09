num_mega = {1,17,23,38,51,53}
num_loto = {1,2,5,7,10,53,23,38,45,51,}

intersecao= num_loto.intersection(num_mega)
diferenca= num_mega.difference(num_loto)
subconjunto = num_loto.issubset(num_mega)

print(intersecao)
print(diferenca)
print(subconjunto)