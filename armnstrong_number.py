# armnstrong number

a = int(input("enter any number : "))

copya=a
sum =0
power = len(str(a))

while(a>0):
    digit = a%10
    sum = sum+digit**power
    a=a//10

if (copya==sum):
    print("this  armnstrong number")
else:
    print("this is not armnstrog number")
