r=0
while r<=4:
    c=0
    while c<=2:
        if (c==0 and r==2) or (c==1 and (r!=0 and r!=4)) or c==2:          
            print('*',end=' ')
        else:
            print(' ',end=' ')
        c=c+1
    print()
    r=r+1