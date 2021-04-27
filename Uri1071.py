def main():

    soma = 0
    X = int(input())
    Y = int(input())
    while X > Y:
        X -= 1
        if X == Y:
            break
        if X % 2 != 0:
            soma = soma + X
    print(soma)


main()
