# ch=input("Enter the character:")
# if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
#     print("it is a vowel")
# else:
#     print("it is an consonant")

# ch=input("Enter the character:")
# if ch>="a" and ch<="z" or ch>="A" and ch<="Z":
#     print("it is a alphabet")
# elif ch>="0" and ch<="9":
#     print("it is a digit")
# else:
#     print("special character")

# ch=input("Enter the character:")
# if ch>="A" and ch<="Z":
#     print("it is uppercase")
# elif ch>="a" and ch<"z":
#     print("it is lowercase")
# else:
#     print("it is invilde")


# week= int(input("Enter the week day(1-7):"))
# if (day==1):
#     print("it is monday")
# elif (day==2):
#     print("it is tuesday")
# elif (day==3):
#     print("it is wenasday")
# elif (day==4):
#     print("it is thrasday")
# elif (day==5):
#     print("it is friday")
# elif (day==6):
#     print("it is satarday")
# elif (day==7):
#     print("it is sunday")
# else:
#     print(" please the weekday number (1-7)")

# a=(12-2004)
# b= -2004
# print(+a)

# Month=int(input("Enter the month number:"))
# if (Month==1):
#     print("day 31")
#     if (Month==2):
#         print("Day 28 or 29")
#         if (Month==3):
#             print("Day 31")
#             if (Month==4):
#                 print("Day 30")
#                 if (Month==5):
#                     print("Day 31")
#                     if (Month==6):
#                         print("Day 30")
#                         if (Month==7):
#                             print("Day 31")
#                             if (Month==8):
#                                 print("Day 31")
#                                 if (Month==9):
#                                     print("Day 30")
#                                     if (Month==10):
#                                         print("Day 31")
#                                         if (Month==11):
#                                             print("Day 30")
#                                             if (Month==12):
#                                                 print("Day 31")
#                                             else:
#                                                 print(1)
#                                         else:
#                                             print(2)
#                                     else:
#                                         print(3)
#                                 else:
#                                     print(4)
#                             else:
#                                 print(5)
#                         else:
#                             print(6)
#                     else:
#                         print(7)
#                 else:
#                     print(8)
#             else:
#                 print(9)
#         else:
#             print(10)
#     else:
#         print(11)
# else:
#     print(12)

# a=int(input("Enetr the first angle triangle:"))
# b=int(input("Enter the second angle triangle:"))
# c=int(input("Enter the third angle triangle:"))
# total=a+b+c
# if total==180:
#     print("it is the validi triangle")
# else:
#     print("it is the invalidi triangle")

# list=[4,5,-8,-3,9,-1,6,-2]
# i=0
# a=[]
# while i<len (list):
#     if list[i]<0:
#         a.append (0)
#     else:
#         a.append(list[i])
#     i=i+1
# print(a)

# a=[1,-2,3,-4,5,-6,7,-8]
# i=0
# b=[]
# while i<len (a):
#     if a[i]<(0):
#         b.append(0)
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)

# a=[10,20,30,40]
# b=[100,200,300,400]
# i=0
# j=1
# while i<len(a):
#     print(a[i],b[-j])
#     j=j+1
#     i=i+1


# a=[10,20,30,[50,60]]
# n=len(a)
# i=0
# while i<n:
#     if type (a[i]) is list:
#         if len(a[i])>1:
#             j=0
#             m=len(a[i])
#             while j<m:
#                 print(i,j,a[i][j])
#                 j=j+1
#             i=i+1
#     else:
#         print(i,a[i])
#         i=i+1
