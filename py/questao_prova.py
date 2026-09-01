#  Questão - o código precisa receber N numeros. Dos N numeros, o código deve fazer
# a maior pontuação. o "jogo" funciona assim: A pontuação começa em 0 e haverá N
# numeros, ao remover um número P, o valor de P é somado a pontuação porém dos números
# é removido P+1 e P-1 que não são somados a pontuação. Após isso ele remove outro
# número, e se repete até acabar todos os numeros.
#   Por exemplo:
# números = {1, 2, 3, 4, 5}
# "remove o 1" pontuação = 1 e sai da lista o 1 e o 2. sobra: {3, 4, 5}
# "remove o 3" pontuação = 4 e sai da lista o 3 e o 4. sobra: {5}
# "remove o 5" pontuação = 9.
#   Outro exemplo:
# números = {3, 3, 5, 4, 2}
# "remove o 3" pontuação = 3 e sai da lista o 3, o 4 e o 2. sobra: {3, 5}
# "remove o 3" pontuação = 6 e sai da lista apenas o 3. sobra: {5}
# "remove o 5" pontuação = 11.