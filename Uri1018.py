def main():
    n = int(input())

    n100 = n//100
    r100 = n%100
    
    n50 = r100//50
    r50 = r100%50
    
    n20 = r50//20
    r20 = r50%20

    n10 = r20//10
    r10 = r20%10

    n5 = r10//5
    r5 = r10%5

    n2 = r5//2
    r2 = r5%2

    n1 = r2
    
    print(n)
    print('{} nota(s) de R$ 100,00'.format(n100))
    print('{} nota(s) de R$ 50,00'.format(n50))
    print('{} nota(s) de R$ 20,00'.format(n20))
    print('{} nota(s) de R$ 10,00'.format(n10))
    print('{} nota(s) de R$ 5,00'.format(n5))
    print('{} nota(s) de R$ 2,00'.format(n2))
    print('{} nota(s) de R$ 1,00'.format(n1))

main()


