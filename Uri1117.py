

x = 1
i = 3
notav = 0
nota = 0
while x < i:
    notav = float(input(""))
    if 0 <= notav <= 10:
            nota = notav + nota
            x = x + 1
    else:
        print("nota invalida")
        notav = notav - notav
print("media = {:.2f}".format(nota/2))
