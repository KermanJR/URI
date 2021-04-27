def main():
  
    N = int(input())
    Y = 0
    counting = 0
    contort = 0
    while Y < N:
        x = int(input())
        if (x >= 10) and (x <= 20):
            Y = Y + 1
            counting += 1
        if x < 0:
            Y = Y + 1
            contort = contort + 1
        if (x > 0) and (x < 10) or (x > 20):
            contort = contort + 1
            Y = Y + 1
    print("{} in".format(counting))
    print("{} out".format(contort))

    
main()

