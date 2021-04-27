def main():

    i = 0
    j = 5
    soma = 0
    while j > i:
        valor = int(input())
        j = j - 1
        if valor % 2 == 0:
            soma += 1

    print("{} valores pares".format(soma))


main()
