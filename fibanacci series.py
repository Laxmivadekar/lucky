a=0
b=1
c=a+b
sum=0
print(a)
print(b)
while c<=1000:
    print(c)
    sum=sum+c
    a=b
    b=c
    c=a+b
print(sum)