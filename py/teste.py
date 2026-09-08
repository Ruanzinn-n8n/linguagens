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


def preencher(sudoku_org):
    sudoku = []
    tam = len(sudoku_org)
    for linha in range(tam):
        new_line = []
        for coluna in range(tam):
            test = sudoku_org[linha][coluna]
            if test != 0:
                new_line.append(test)
            else:
                for i in range(tam):
                    if i not in sudoku_org[linha]:
                        for j in range(tam):
                            if j != sudoku_org[j][coluna]:
                                test = j
                new_line.append(test)
        sudoku.append(new_line)
    return sudoku

resul = preencher(sudoku)
for i in resul:
    print(*i)