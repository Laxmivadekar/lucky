i=1
while i<=5:
    if i==1:
        print(' '*(5-i)+"*")
    elif i==5:
        print('*'*(2*i-1))
    else:
        print(' '*(5-i)+'*'+' '*(2*i-3)+'*')
    i=i+1