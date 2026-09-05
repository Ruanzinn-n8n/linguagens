matriz = [
    [],
    [],
    [],
]
for i in range(3):
    matriz[i] = list(map(int, input(f"Digite a {i+1}° linha: ").split()))
for i in matriz:
    print(i)