def main():

    NUM_V = input()
    SAL_F = float(input())
    TV_E = float(input())

    TOTAL = (15 / 100 * TV_E) + SAL_F

    print("TOTAL = R$ {:.2f}".format(TOTAL))


main()