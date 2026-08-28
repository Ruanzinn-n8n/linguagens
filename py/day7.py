#vou usar os comentários apenas para voce indentificar qual exercicio é qual, pode ignorar eles.

# Exercicio 1
"""n = int(input())
numeros = []
for i in range(n):
    numeros.append(int(input()))
numeros.sort()
print(f"Maior: {numeros[n-1]}")
print(f"Menor: {numeros[0]}")
print(numeros)
"""

# Exercicio 2
"""n = int(input())
nums = list(map(int, input().split()))
dif = set(nums)
print(len(dif))
"""

# Exercicio 3
"""numeros = list(map(int, input().split()))
maior = numeros[0]
for i, numero in enumerate(numeros):
    if numero > maior:
        maior = numero
print(i, maior)
#travei em mostrar a primeira vez
"""

# Exercicio 4
nomes = list(input().split())
notas = list(map(int, input().split()))
for nome, nota in zip(nomes, notas):
    print(nome, nota)