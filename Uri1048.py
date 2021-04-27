def main():
  
  
    s = float(input())

    if s > 0 and s <= 400.00:
        print("Novo salario: {:.2f}".format(s + s*0.15))
        print("Reajuste ganho: {:.2f}".format(s*0.15))
        print("Em percentual:", format(0.15*100,'.0f'), "%")

    if s >= 400.01 and s <= 800.00:
        print("Novo salario: {:.2f}".format(s + s*0.12))
        print("Reajuste ganho: {:.2f}".format(s*0.12))
        print("Em percentual:", format(0.12*100,'.0f'), "%")

    if s >= 800.01 and s <= 1200.00:
        print("Novo salario: {:.2f}".format(s + s*0.10))
        print("Reajuste ganho: {:.2f}".format(s*0.10))
        print("Em percentual:", format(0.10*100,'.0f'), "%")


    if s >= 1200.01 and s <= 2000.00:
        print("Novo salario: {:.2f}".format(s + s*0.07))
        print("Reajuste ganho: {:.2f}".format(s*0.07))
        print("Em percentual:", format(0.07*100,'.0f'), "%")
    
    if s > 2000.00:
        print("Novo salario: {:.2f}".format(s + s*0.04))
        print("Reajuste ganho: {:.2f}".format(s*0.04))
        print("Em percentual:", format(0.04*100,'.0f'), "%")
    


main()
