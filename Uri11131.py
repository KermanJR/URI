

x = 1
i = 0
intern = 0
grem = 0
grenal = 0
vi = 0
vg = 0
emp = 0
while x > i:
    inter, gremio = input().split()
    inter, gremio = int(inter), int(gremio)
    if inter > gremio:
        vi += 1
    if inter < gremio:
        vg += 1
    if inter == gremio:
        emp += 1
    grenal = grenal + 1
    grem = gremio + grem
    intern = inter + intern
    print("Novo grenal (1-sim 2-nao)")
    z = int(input())
    if z == 1:
        continue
    if z == 2:
        break
print("{} grenais".format(grenal))
print("Inter:{}".format(vi))
print("Gremio:{}".format(vg))
print("Empates:{}".format(emp))
if vi > vg:
        print("Inter venceu mais")
if vg > vi:
        print("Gremio venceu mais")

