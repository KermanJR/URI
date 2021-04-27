def main():

    N = 0
    contador = 0
    soma = 0
    while N < 6:
        x = float(input(""))
        if x > 0:
            N = N + 1
            contador = contador + 1
            soma = soma + x
        if x < 0:
            N = N + 1
    print("{} valores positivos".format(contador))
    media = soma/contador
    print("{:.1f}".format(media))
    
    
main()
