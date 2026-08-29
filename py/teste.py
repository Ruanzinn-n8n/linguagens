def trocar(frase):
    trocada = []
    if len(frase) % 2 == 0:
        for i in range(0, len(frase), 2):
            trocada.append(frase[i+1])
            trocada.append(frase[i])
    else:
        for i in range(0, len(frase), 2):
            if i == len(frase)-1:
                trocada.append(frase[i])
            else:
                trocada.append(frase[i+1])
                trocada.append(frase[i])
    return trocada

texto = list(input().split())
new_f = trocar(texto)
frase_j = " ".join(new_f)
print(frase_j)