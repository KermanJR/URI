
while True:
    try:
        x = input()
        z = 0
        for i in range(len(x)):
            if x[i] == '(':
                z += 1
            elif x[i] == ')':
                z -= 1
            if z < 0:
                break
        if z != 0:
            print('incorrect')
        else:
            print('correct')

    except EOFError:
        break
