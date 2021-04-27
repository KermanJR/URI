def main():

    N = int(input())
    a = N//365
    rd = N%365
    m = rd//30
    rm = rd%30
    d = rm

    print('{:.0f} ano(s)'.format(a))
    print('{} mes(es)'.format(m))
    print('{} dia(s)'.format(d))


main()
