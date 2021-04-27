import math

def main():

    valor = float(input())
    print("NOTAS:")

    notas = math.floor(valor/100.0)
    valor -= notas*100
    print("%d nota(s) de R$ 100.00" % notas)

    notas = math.floor(valor/50.0)
    valor -= notas*50
    print("%d nota(s) de R$ 50.00" % notas)

    notas = math.floor(valor/20.0)
    valor -= notas*20
    print("%d nota(s) de R$ 20.00" % notas)

    notas = math.floor(valor/10.0)
    valor -= notas*10
    print("%d nota(s) de R$ 10.00" % notas)

    notas = math.floor(valor/5.0)
    valor -= notas*5
    print("%d nota(s) de R$ 5.00" % notas)

    notas = math.floor(valor/2.0)
    valor -= notas*2
    print("%d nota(s) de R$ 2.00" % notas)

    print("MOEDAS:")

    moedas = math.floor(valor/1.0)
    valor -= moedas*1
    valor = round(valor, 2)
    print("%d moeda(s) de R$ 1.00" % moedas)

    moedas = math.floor(valor/0.50)
    valor -= moedas*0.50
    valor = round(valor, 2)
    print("%d moeda(s) de R$ 0.50" % moedas)

    moedas = math.floor(valor/0.25)
    valor -= moedas*0.25
    valor = round(valor, 2)
    print("%d moeda(s) de R$ 0.25" % moedas)

    moedas = math.floor(valor/0.10)
    valor -= moedas*0.10
    valor = round(valor, 2)
    print("%d moeda(s) de R$ 0.10" % moedas)

    moedas = math.floor(valor/0.05)
    valor -= moedas*0.05
    valor = round(valor, 2)
    print("%d moeda(s) de R$ 0.05" % moedas)

    moedas = math.floor(valor/0.01)
    valor -= moedas*0.01
    valor = round(valor, 2)
    print("%d moeda(s) de R$ 0.01" % moedas)
    

main()
