print("Questão 3 - Segundo Maior")
print("")

def segundo_maior(numeros):
    maior = numeros[0]
    s_maior = numeros[0]
    for i in numeros:
        if i > maior:
            maior = i
    for i in numeros:
        if i > s_maior and i < maior:
            s_maior = i
    return s_maior

lista = []
print("Digite 6 números;")
for i in range(6):
    lista.append(int(input(f"N°{i+1}: ")))
print("")
print(segundo_maior(lista))
print("")