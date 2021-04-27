def main():
  
  
    N = int(input())
    hrs = N//3600
    r = N%3600
    min = r//60
    r = r%60
    seg = r

    print('{:.0f}:{:.0f}:{:.0f}'.format(hrs, min, seg))


main()
