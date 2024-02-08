sum=0
num=int(input("enter the num: "))
num1=num
while(num>0):
    r=num%10
    cube=r*r*r
    sum=sum+cube
    q=num//10
    num=q

if num1==sum:
    print("given number is armstrong")
else:
    print("given number is not armstrong number")
