# desafios de fixação do conteúdo dos ultimos 4 dias

# 01
"""print("--------------------------")
print("O numero misterioso...")
print("--------------------------")
print("")
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
par = 0
impar = 0
soma = 0

for i in num:
    num[i] = int(input(f"Digite o {i+1}º número: "))
    soma += num[i]
    if num[i] % 2 == 0:
        par += 1
    else:
        impar += 1

maior = num[0]
menor = num[0]

for i in num:
    if i > maior:
        maior = i

    if i < menor:
        menor = i

print("")
print("---------------------------------------")
print(f"O {maior} é o maior número.")
print(f"O {menor} é o menor número.")
if par != 1:
    print(f"Tem {par} números pares.")
else:
    print(f"Tem {par} número par")

if impar != 1:
    print(f"Tem {impar} números ímpares.")
else:
    print(f"Tem {impar} número ímpar.")
print("-------------------------------------")
"""
print("")

# 02
print("Saque")
print("")
print("Digite o valor que deseja sacar:")
saque = int(input())
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0