def main():
  
  
    s = float(input())

    if 0.00 <= s <=2000:
        print('Isento')

    elif 2000.01<= s <= 3000.00:
        diferenca = s - 2000
        ir = (8/100)*diferenca
        print("R$ {:.2f}".format(ir)) 
        
    elif 3000.01 <= s <= 4500.00:
        diferenca = s - 3000
        ir2 = (18/100)*diferenca + (8/100)*1000
        print("R$ {:.2f}".format(ir2))

    elif 4500.00 < s:
        ir3 = (s - 4500)*(28/100) + (8/100)*1000 + (18/100)*1500
        print("R$ {:.2f}".format(ir3))
    


main()
