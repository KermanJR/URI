

N = int(input())
i = 0
while i < N:
    x1, y1, z1 = input().split()
    x1, y1, z1 = float(x1), float(y1), float(z1)
    p1 = 2
    p2 = 3
    p3 = 5
    i = i + 1
    mp = ((x1 * p1) + (y1 * p2) + (z1 * p3)) / (p1 + p2 + p3)
    print("{:.1f}".format(mp))

