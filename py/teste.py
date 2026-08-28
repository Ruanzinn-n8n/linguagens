print("Rec 1 - concluida")
print("")

def num_bin(num):
    bin = []
    while num != 0:
        sobra = num % 2
        bin.append(sobra)
        num = num // 2
    return bin
def inverter(lista):
    bin = []
    tam = len(lista) -1
    for i in range(len(lista)):
        n_oposto = tam -i
        bin.append(lista[n_oposto])
    return bin

n = 0
while n <= 0:
    n = int(input("Digite o número para conversão: "))
    if n <= 0:
        print("Número inválido, digite um número maior que 0!")

num = num_bin(n)
n_binario = inverter(num)
str_bin = []
for i in n_binario:
    n_bin = str(i)
    str_bin.append(n_bin)
j_bin = "".join(str_bin)
print(j_bin)