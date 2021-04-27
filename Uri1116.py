

N = int(input())
while N > 0:
    x, y = input().split()
    x, y = float(x), float(y)
    if y != 0:
        div = x / y
        N = N - 1
        print("{:.1f}".format(div))
    else:
        print("divisao impossivel")
        N = N - 1








