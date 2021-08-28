num=1
while num<=100:
    sum=0
    temp=num
    while temp>0:
        rem=temp%10
        sum=sum+rem
        temp=temp//10
    if num%sum==0:
        print(num)
    num=num+1