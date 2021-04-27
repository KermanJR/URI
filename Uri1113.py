

x = 1
i = 0
while x > i:
    a, b = input().split()
    a, b = int(a), int(b)
    if a > b:
        print("Decrescente")
    if b > a:
        print("Crescente")
    if b == a:
        break
    x = x + 1
