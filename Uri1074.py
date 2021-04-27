

n = 0
z = int(input())
while n < z:
    x = float(input())
    if x % 2 == 0:
        if x > 0:
            print("EVEN POSITIVE")
            n = n + 1
        if x < 0:
            print("EVEN NEGATIVE")
            n = n + 1
        if x == 0:
            print("NULL")
            n = n + 1
    if x % 2 != 0:
        if x > 0:
            print("ODD POSITIVE")
            n = n + 1
        else:
            print("ODD NEGATIVE")
            n = n + 1
