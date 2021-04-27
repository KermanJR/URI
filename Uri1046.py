

hi, hf = input().split()
hi = int(hi)
hf = int(hf)
if hi > hf:
    a = 24 - hi
    h = a + hf
    print("O JOGO DUROU {} HORA(S)".format(h))
elif hf > hi:
    h = hf - hi
    print("O JOGO DUROU {} HORA(S)".format(h))
elif hi == hf:
    h = 24
    print("O JOGO DUROU {} HORA(S)".format(h))

