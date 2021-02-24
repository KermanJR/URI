def main():

    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)

    MAB = (A + B + abs(A - B)) / 2
    MAB_C = (C + MAB + abs(C - MAB)) / 2

    print("%i eh o maior" % MAB_C)


main()