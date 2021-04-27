

maior = 0
lista = {}
posicao = 0
while posicao < 100:
    num = int(input())
    if num > maior:
        maior = num
        lista[num] = posicao
    posicao += 1
print(maior)
print(lista[maior]+1)
