# revers number

a= int(input("enter any number for revers : "))
rev=0
while(a>0):
    rev=(rev*10)+a%10
    a=a//10
print("the revers number is ",rev)