entrada = "5,3,0,0,7,0,0,0,0,6,0,0,1,9,5,0,0,0,0,9,8,0,0,0,0,6,0,8,0,0,0,6,0,0,0,3,4,0,0,8,0,3,0,0,1,7,0,0,0,2,0,0,0,6,0,6,0,0,0,0,2,8,0,0,0,0,4,1,9,0,0,5,0,0,0,0,8,0,0,7,9"

list_inp = list(map(int, entrada.split(",")))
sudoku = []
tam = len(list_inp)
for i in range(0, tam, 9):
    linha_subs = []
    for j in range(9):
        n = i+j
        linha_subs.append(list_inp[n])
    sudoku.append(linha_subs.copy())
for i in sudoku:
    print(*i)