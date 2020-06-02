x=int(input('輸入層數'))

for i in range(1,x+1):
    for k in range(i,x):
        print(" ",end='')
    for j in range(1,2*i):
        print('*',end='')
    print("")

for i in range(0,x):
    for k in range(1,x-1):
        print(' ',end='')
    for j in range(0,3):
        print('*',end='')
    print('')
