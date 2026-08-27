print("Questão 6 - Dicionário")
print("")

def dicionario(valores):
    cont = 0
    soma = 0
    maior = 0
    for i in valores:
        soma += valores[i]
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] >= 7:
            cont += 1
    media = soma/4
    menor = maior
    for i in valores:
        if valores[i] < menor:
            menor = valores[i]
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Média da turma: {media}")
    print(f"Alunos aprovados: {cont}")

alunos = {
    "Ruan": 8.5,
    "Lucas": 6.0,
    "Higor": 9.2,
    "Samira": 7.8
}

dicionario(alunos)
#não deu certo n sei porque, mas acredito que seja uma coisa simples, porém acho que já tentei tudo que sei.
print("")