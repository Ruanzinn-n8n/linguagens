lista = [1, 2, 3, 2, 5, 2]
busca = int(input("digite: "))

for i in lista:
    if i == busca:
        posicao = lista.index(i)
        print(posicao)