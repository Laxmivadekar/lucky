n=100
while n<=1000:
    temp=n
    sum=0
    while temp>0:
        rem=temp%10
        sum+=rem**3
        temp//=10
    if sum==n:
        print(n)
    n=n+1
    
