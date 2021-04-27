def main():
  
    c, qtd = input().split()
    c = int(c)
    qtd = int(qtd)

    if c == 1:
        print("Total: R$ {:.2f}".format(4.00*qtd))

    if c == 2:
        print("Total: R$ {:.2f}".format(4.50*qtd))

    if c == 3:
        print("Total: R$ {:.2f}".format(5.00*qtd))

    if c == 4:
        print("Total: R$ {:.2f}".format(2.00*qtd))
   
    if c == 5:
        print("Total: R$ {:.2f}".format(1.50*qtd))

        
main()
  
  

  
  
  
  
  
  
