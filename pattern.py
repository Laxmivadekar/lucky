n=int(input('enter a number'))
i=0
while i<=n:
    print(' '*(n-i-1)+'* ',end='')
    if i>=1:
        print(' '*(2*i-1)+'* ',end='')
    i=i+1
    print( )
    