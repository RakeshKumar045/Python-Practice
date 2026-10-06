# prime number with for loop recurssion method is know as lop method

a = int(input("enter any number for prime : "))

if a==0 or  a==1:
    print(" it is not prime number it start frm 2 number ")
elif a >1:
    for i in range (2,a):
        if a%i==0:
            print("it is not prime number")
            break
    else:
        print("this is prime number")

else:
    print("it is not prime number")

