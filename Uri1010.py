def main():


    cod_1, num_1, val_1 = input().split()
    cod_1 = int(cod_1)
    num_1 = int(num_1)
    val_1 = float(val_1)

    cod_2, num_2, val_2 = input().split()
    cod_2 = int(cod_2)
    num_2 = int(num_2)
    val_2 = float(val_2)

    print("VALOR A PAGAR: R$ {:.2f}".format(num_1 * val_1 + num_2 * val_2))


main()