# ch=input("Enter the charecter:")
# if ch>="A" and ch<="Z":
#     print("it is uppercase")
# elif ch>="a" and ch<="z":
#     print("it is lowercase")
# else:
#     print("incorret")

# num=int(input("Enter the number:"))
# if num>1:
#     print("it is postive number")
# elif num==0:
#     print("it is zero number")
# else:
#     print("it is negatevi number")

# ch= input("Enter a character: ")
# if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
#  or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
#     print(ch, "is a Vowel")
# else:
    # print(ch, "is a Consonant")

# a=int(input("Enter the angle of a triangle:"))
# b=int(input("Enter the angle of a triangle:"))
# c=int(input("Enter the angle of a triangle:"))
# total=a+b+c
# if total==180:
#     print("it is triangle")
# else:
#     print("it is not triangle")

# ch= input("Enter a character:")
# if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
#     print("it is alphabet")
# elif ch>="0" and ch<="9":
#     print("it is digite")
# else:
#     print("it is special character")

# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# c=int(input("Enter the number:"))
# if a>=b and b<=a:
#     print(a," is maximum number")
# elif b<=c and c>=b:
#     print(b,"is maximum number")
# else:
#     print(c," is not maximum number")

# num=int(input("Enter the number:"))
# if num%5==0:
#     print("num divisibel by 5")
# elif num%11==0:
#     print("num divisibal by 11")
# else:
#     print("num not divisebal 5 and 11")

# a=int(input("Enetr the leep year:"))
# if a%4==0 or a%400==0:
#     print("it is leep year")
# else:
#     print("it is not leep year")

# a=int(input("Marks is physics:"))
# b=int(input("Marks is chemistry:"))
# c=int(input("Marks is biology:"))
# d=int(input("Marks is mathematics:"))
# e=int(input("Marks is computer:"))
# f=int(input("Marks is sixth:"))
# total=a+b+c+d+e
# percentage=(total/500*100)
# print("Total Marks=","percentage", percentage)
# if (percentage<=90):
#     print("your is grade A")
#     if (percentage<=80):
#         print("your is grade B")
#         if (percentage<=70):
#             print("your is grade C")
#             if (percentage<=60):
#                 print("your is grade D")
#                 if (percentage<=50):
#                     print("your is grade E")
#                 else:
#                     print("your is grade F")
#             else:
#                 print("your is grade E")
#         else:
#             print("your is grade C")
#     else:
#         print("your is grade B")
# else:
#     print("your is grade A")

# num=int(input("Enter the number:"))
# if num>0:
#    print(num%100//1,"it is last digit")
# else:
#     print( num,"it is not last digit")

# a=int(input("enter the number:"))
# i=0
# while (i<=10):
#     i=i+1
#     if i%2==0:
#         print(i,"even number")
#     else:
#         print(i,"odd number")

# i=0
# while i<=10:
#     print(i)
#     i=i+1

# i=10
# while i>=1:
#     print(i)
#     i=i-1
                                      
# a=[2,1,4,6,7,3]
# print(len(a))

# num1=int(input("enter the number:"))
# num2=str(num1)
# i=0
# while i<len(num2):
#     a=(int(num2[i])**2)
#     print(a,end=" ")
#     i=i+1
# print()

# list1 = [6,1,3,5,6,7,8,3,1]
# a=[]
# for i in list1:
#     if i not in a:
#         a.append(i)
# print(a)



# name= "pinke is a good girl"
# words=name.split()
# words=list(reversed(words))
# print(" ".join(words))

# a=name.split()
# print(a)
# l=len(name)
# i=1
# while i>len(name[i]):
#     rev=name[-i]
#     i=i+1
#     print(" ".join(words))
 
# list=[1,2[3,4,5],[6,7,8,9]]
# print(list,[1][1])

# a=["python",1,2,3,True]
# i=0
# while i<len(a):
#     if i==True:
#         print("python")
#     i=i+1

# a=[1,2,3,4,5]
# b=[11,22,33,44,55]
# i=0
# j=1
# while i<len(a):
#     print(a[i],b[-j])
#     j=j+1
#     i=i+1
# print()

# a=[1,2,3,4,5]
# i=0
# sum=0
# while i<len(a):
#     sum=sum*a[i]
#     i=i+1
# print(sum)

# list=[2,54,7,8,9,45,3,56]
# j=0
# k=[]
# c=[]
# while j<len(list):
#     i=1
#     count=0
#     while i<=list[j]:
#         if list[j]%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         k.append(list[j])
#     else:
#         c.append(list[j])
#     j+=1
# print("it is prime number:",k)
# print("it is not prime number:",c)

# a=[1,2,3,4,5,6,7]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# list=[1,-2,3,-4,5,-6,7,-8]
# i=0
# a=[]
# while i<len(list):
#     if list[i]<0:
#         a.append(0)
#     else:
#         a.append(list[i])
#     i=i+1
# print(a)

# i=0
# while i<5:
#     j=1
#     while j<i:
#         print(j,end=" ")
#         j=j+1
#     i=i+1
# print()

# i=1
# while i<=30:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j )
#         j=j+1
#     i=i+1
# print( )

# list=[1,-2,3,-4,5,-6,7,-8]
# i=0
# a=[]
# while i<len(list):
#     if list[i]>0:

#         a.append(0)
#     else:
#         a.append(list[i])
#     i=i+1
# print(a)


# list1=[10,20,30,40]
# list2=[100,200,300,400]
# i=0
# j=1
# while i<len(list1):
#     print(list1[i],list2[-j])
#     j=j+1
#     i=i+1

# a=["my",29,32.2,"number",23+2j,23,45,"name"]

# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==str or type(a[i])==complex:
#         b.append(a[i])
#     i=i+1
# print(b) 


# a=[1,2,3,4,5,5,2,5,1,3,4,1,6,2,1,3,1,456,456,6789,6789]
# b=[]
# i=0
# while i<len(a):
#     n=a[i]
#     j = 0
#     c = 0
#     while j<len(a):
#         if a[i] == a[j] and i!=j:
#             c+=1
#         j+=1
#     if c>=1:
#         if n not in b:
#             b.append(n)
#     i+=1
# print(b)                                                                                                                                                                               

# list=[1,2,3,4,5,6,7,8]
# num=int(input("Enter the number:"))
# i=num
# while i>=1:
#     print(i)
#     i=i-1


# a=[2,3,5,6,8,1,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[i]>a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
#         j=j+1
#     i=i+1
# print(a)

# a=[10,20,30,40,50]
# b=[100,200,300,400,500]
# i=0
# j=1
# while i<len(a):
#     print(a[i],b[-j])
#     j=j+1
#     i=i+1
# print(a)


# i=0
# j=1
# while i<len(b):
#     print(a[-i],b[-j])
#     j=j+1
#     i=i+1
# print(a)

# a=[1,2,3,4,5,6,7,8]
# i=0
# while i<len(a):
#     i=i+1
# print(a)

# a=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<=10:
#     i=i+1
# print(a)


# a=30 or 40+3**2//(3+False)
# print(a)
