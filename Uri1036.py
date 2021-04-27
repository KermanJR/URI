import math

def main():
  

    A, B, C = input().split()
    A = float(A)
    B = float(B)
    C = float(C)

    D = B*B-4*A*C

    if (D < 0 or A == 0):
        print("Impossivel calcular")

    else:

        R1 = (-B + math.sqrt(D))/(2*A)
        print("R1 = {:.5f}".format(R1))

        R2 = (-B - math.sqrt(D))/(2*A)
        print("R2 = {:.5f}".format(R2))
        

main()



    
