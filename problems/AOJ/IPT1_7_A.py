while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        quit()
    
    if m == -1 or f == -1:
        print('F')
    else:
        s = m+f
        if s >= 80:
            print('A')
        elif s < 80 and s >= 65:
            print('B')
        elif s < 65 and s >= 50:
            print('C')
        elif s < 50 and s >= 30:
            if r >= 50:
                print('C')
            else:
                print('D')
        elif s < 30:
            print('F')
