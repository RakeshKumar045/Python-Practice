# list practices  remove the duplicate

# l = [4,5,6,7,0,4,7,9]
# l1=[]
# for m in l:
#     if m not in l1:
#         l1.append(m)
# print(l1)
#  want to print reverse number
# n=7245
# rev = 0
# while n>=1:
#     rev= (rev*10 )+ n%10
#     n=n//10
#     print(" this is reverse ",n)
#
#  calculater
# a=int(input("enter first num"))
# sign = input("enter the sign ,+-*/")
# b=int(input("enter second num"))

# if sign == "+" :
#     print("addition",a+b)
# elif sign =="-":
#     print("minus",a-b)
# elif sign =="*":
#     print("multiple",a*b)
# elif sign  =="/":
#     print("divde",a/b)
# else:
#     print("defalut entery")

#  finf the max from list
l2 = [5,7,0,9]
l3 = max(l2)
print(l3)

# add two list
l5=[5,2,4]
l6=[5,3,6]

l7 =[]
for i in  range (len(l5)):
    l7.append(l5[i]+l6[i])
print(l7)

# # revers the list item
# l9 = [7,9,2,1,0]
# l10 = []
# for i in range (len(l9)):
#     leng = len(l9)
#     print(append.(l9[leng-i-1])
#     print(l10.append(l9[leng-i-1])

l11= [1,8,0]

temp = l11[0]
l11[0]=l11[2]
l11[2]=temp
print(l11)

#  find the item iin this

v= ("k","l","t")
if "l" in v:
    print("yes it is present")

else:

    print("not present ")

s = " thi is good "
if "thi" in s:
    print("yes ***present ")
else:
    print("not present ")


print("w*100")

s= " this is good time yes "

s3 =s.split()
s4 =[]

for i in  range (len(s3)):
    leng = len(s3)
    print(s3[leng-i-1])
print(s4.append(s3[leng-i-1]))

s5 = " thisNotrightmethoD"
l44 =len(s5)
print(l44)

s6 =""
lengt=len(s5)
for i in range (len(s5)):
    if i>=lengt//2:
        s6=s6+s5[i].lower()
    else:
        s6=s6+s5[i].upper()
print(s6)

# s1 = "thismybook"
# s11= s1.replace("m","9")
# print(s11)

v = intput("t","h","y")
if ch in ("t","h","y"):
    print(v)







