n=int(input('enter a number'))
sum=0
temp=n
while temp>0:
    rem=temp%10
    sum+=rem**3
    temp//=10
if n==sum:
    print('num,it is arm strong')
else:
    print('num,it is not arm strong')