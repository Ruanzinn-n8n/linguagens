# aprendendo mais sobre if, elif e else. suas condições e operadores.

# Exercicio 1 - 10xp
print("Exercicio 1 concluido")
"""print("")
idad = int(input("Quantos anos você tem? "))

if idad >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
"""
print("")

# Exercicio 2 - 10xp
print("Exercicio 2 concluido")
"""print("")
num = int(input("Digite um numero inteiro: "))

if num > 0:
    print(f"{num} é um inteiro POSITIVO")
elif num < 0:
    print(f"{num} é um inteiro NEGATIVO")
else:
    print("ZERO")
"""
print("")

# Exercicio 3 - 15xp
print("Exercicio 3 concluido")
"""print("")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

print("")
if media >= 7:
    print(f"Sua média é {media:.2f}, você foi APROVADO")
elif media < 5:
    print(f"Sua média é {media:.2f}, você foi REPROVADO")
else:
    print(f"Sua média é {media:.2f}, voce está de RECUPERAÇÃO")
"""
print("")

# Exercicio 4 - 20xp
print("Exercicio 4 concluido")
"""print("")
print("---- Classificação de idade ----")
print("")
idade = int(input("Qual sua idade? "))
print("")

if idade <= 12:
    print(f"Você tem {idade} anos, é uma criança.")
elif idade <= 17:
    print(f"Você tem {idade} anos, é um adolescente.")
elif idade <= 59:
    print(f"Você tem {idade} anos, é um adulto.")
else:
    print(f"Você tem {idade} anos, é idoso.")
"""
print("")

# Exercicio 5 - 20xp
print("Exercicio 5 concluido")
"""print("")
print("---- Quer dirigir? ----")
print("")
idades = int(input("Quantos anos você tem? "))
cnh = input("Possui CNH? ")
sim = "Sim", "sim", "s", "S", "yes", "Yes", "SIM"
nao = "Nao", "Não", "nao", "não", "n", "N", "no", "NO"

if idades >= 18 and cnh in sim:
    print(f"Você tem {idades} anos e possui a CNH.")
    print("=== Pode dirigir ===")
elif idades >= 18 and cnh in nao:
    print(f"Você tem {idades} anos mas não possui a CNH.")
    print("=== Não pode dirigir ===")
else:
    print("Você é menor de idade, logo não tem permissão para dirigir!")
    """
print("")