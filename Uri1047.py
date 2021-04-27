from math import floor

def main():
  
    hi, mi, hf, mf = input().split()
    hi, mi = int(hi), int(mi)
    hf, mf = int(hf), int(mf)

    if (hi == hf and mi== mf):
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        mt = (60*hf + mf - 60*hi - mi) % 1440
        ht = floor (mt/60)
        mt -= ht *60

        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(ht, mt))

        
main()
