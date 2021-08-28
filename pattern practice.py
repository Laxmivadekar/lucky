n=int(input('enter a number'))
i=1
j=1
while i<=5:
    k=1
    while k<=4:
        print(j,end='')
        k=k+1
        while j<=3:
            print(k,end='')
            j=j+1
        n=n+1
    print()
    i=i+1