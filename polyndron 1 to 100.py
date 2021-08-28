n=1
while n<=100:
    temp=n
    rev=0
    while rev<=temp:
        rem=temp%10 
        rev=(rev*10)+rem
        temp=temp//10
    if rev==n:
        print(n)
    n=n+1