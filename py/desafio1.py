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
"""print("Saque")
print("")
print("Digite o valor que deseja sacar:")
saque = int(input())
print("")
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

if saque < 0:
    print("Você ta lascado KKKKKKKKK")

else:
    while saque >= 100:
        cem += 1
        saque -= 100
    while saque >= 50:
        cinq += 1
        saque -= 50
    while saque >= 20:
        vinte += 1
        saque -= 20
    while saque >= 10:
        dez += 1
        saque -= 10
    while saque >= 5:
        cinco += 1
        saque -= 5
    while saque >= 2:
        dois += 1
        saque -= 2
    while saque >= 1:
        um += 1
        saque -= 1

if cem != 0:
    print(f"Notas de cem: {cem}")
if cinq != 0:
    print(f"Notas de cinquenta: {cinq}")
if vinte != 0:
    print(f"Notas de vinte: {vinte}")
if dez != 0:
    print(f"Notas de dez: {dez}")
if cinco != 0:
    print(f"Notas de cinco: {cinco}")
if dois != 0:
    print(f"Notas de dois: {dois}")
if um != 0:
    print(f"Notas de um: {um}")
"""
print("")

#3

#4

#5

#6
print("Notas da turma")
print("-----------------")
medias = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Digite a nota dos alunos")

print("Aluno 1:")
nota1 = int(input("--- Nota 1: "))
nota2 = int(input("--- Nota 2: "))
medias[0] = (nota1 + nota2)/2
print(f"Média: {medias[0]}")

print("")
print("Aluno 2:")
nota3 = int(input("--- Nota 1: "))
nota4 = int(input("--- Nota 2: "))
medias[1] = (nota3 + nota4)/2
print(f"Média: {medias[1]}")

print("")
print("Aluno 3:")
nota5 = int(input("--- Nota 1: "))
nota6 = int(input("--- Nota 2: "))
medias[2] = (nota5 + nota6)/2
print(f"Média: {medias[2]}")

print("")
print("Aluno 4:")
nota7 = int(input("--- Nota 1: "))
nota8 = int(input("--- Nota 2: "))
medias[3] = (nota7 + nota8)/2
print(f"Média: {medias[3]}")

print("")
print("Aluno 5:")
nota9 = int(input("--- Nota 1: "))
nota10 = int(input("--- Nota 2: "))
medias[4] = (nota9 + nota10)/2
print(f"Média: {medias[4]}")

print("")
print("Aluno 6:")
nota11 = int(input("--- Nota 1: "))
nota12 = int(input("--- Nota 2: "))
medias[5] = (nota11 + nota12)/2
print(f"Média: {medias[5]}")

print("")
print("Aluno 7:")
nota13 = int(input("--- Nota 1: "))
nota14 = int(input("--- Nota 2: "))
medias[6] = (nota13 + nota14)/2
print(f"Média: {medias[6]}")

print("")
print("Aluno 8:")
nota15 = int(input("--- Nota 1: "))
nota16 = int(input("--- Nota 2: "))
medias[7] = (nota15 + nota16)/2
print(f"Média: {medias[7]}")

print("")
print("Aluno 9:")
nota17 = int(input("--- Nota 1: "))
nota18 = int(input("--- Nota 2: "))
medias[8] = (nota17 + nota18)/2
print(f"Média: {medias[8]}")

print("")
print("Aluno 2:")
nota19 = int(input("--- Nota 1: "))
nota20 = int(input("--- Nota 2: "))
medias[9] = (nota10 + nota20)/2
print(f"Média: {medias[9]}")

media_t = (medias[0] + medias[1] + medias[2] + medias[3] + medias[4] + medias[5] + medias[6] + medias[7] + medias[8] + medias[9])/10

maio = medias[0]
meno = medias[0]
apr = 0
rec = 0
rep = 0
for i in medias:
    if maio < i:
        maio = i
    if meno > i:
        meno = i

    if i >= 7:
        apr += 1
    elif i >= 5:
        rec += 1
    else:
        rep += 1

print("")
print("")
print("===== Turma A =====")
print("-------------------")
print(f"Média da turma: {media_t}")
print(f"Maior nota: {maio}")
print(f"Menor nota: {meno}")
print(f"Aprovados: {apr}")
print(f"Recuperação: {rec}")
print(f"Reprovados: {rep}")