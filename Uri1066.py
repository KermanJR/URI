def main():
  
  
    par = 0
    imp = 0
    posit = 0
    neg = 0
    Z = 0
    while Z < 5:
        x = int(input())
        if x % 2 == 0:
            par = par + 1
        if x % 2 != 0:
            imp = imp + 1
            Z = Z + 1
        if x == 0:
            Z = Z + 1
        if x > 0:
            posit = posit + 1
            Z = Z + 1
        if x < 0:
            neg = neg + 1
    print("{} valor(es) par(es)".format(par))
    print("{} valor(es) impar(es)".format(imp))
    print("{} valor(es) positivo(s)".format(posit))
    print("{} valor(es) negativo(s)".format(neg))


main()




