# a=["amisha","tanu","ammu","apple","orange","banana"]
# print (a[2])
# print (a[-2])
# print (a[0:5])
# print(a[4:])

# a=["amisha","tanu","ammu","apple","banana"]
# a[3]="cherry"
# print(a)

# a=[1,2,3,4,5,6]
# i=0
# sum=0
# while(i<len(a)):
#     sum=sum+a[i]
#     i=i+1
# print(sum)



# a=["sita","ram","ravan","maruti"]
# a.remove("ram")
# print(a)
# del[]
# print(a)
# del a[0]
# print(a)

# a=[2,4,5,6,7,8,9,1]
# del a[0]
# print(a)


# print(a)
# a.clear()
# print(a)


# a.pop()
# print(a)


# a.sort()
# print(a)

# a=[]
# del []
#
# print(a)


# b=["amisha","jagu","tanu","ammu"]
# b=[2,37,8,12,89,23.4]
# a=b.copy()
# print(a)


# Join Two Lists

# a=["d","s","v","l"]
# b=[12,43,56,87]
# c=a+b
# print(c)


# a=["apple","banana","amisha","tanu"]
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1


# i=0
# while(i<=9):
#     i=i+1
#     if(i==2):
#         continue
#     elif(i==4):
#         continue
#     elif(i==6):
#         continue
#     elif(i==8):
#         continue
#     else:
#         print(i)


# name = ["Savitri", "Phule", "26"]
# print (name[0]+name[1]+name[2])


# name= input("entre a name:"))
# if (name% 2==0):
#     print(name,"is an even")
# else:
#     print(name,"is an odd") 



# name=input("enter the name:")
# Length=len(name)
# if Length%2==0:
#     print("It is even")
# else:
#     print("It is odd")


# name=["amisha","tanu","ammu","meera"]
# a=len(name)
# print(a)
# i=0
# while i<len(name):
#     if i%2==0:
#         print(name[i],"even")
#     else:
#         print(name[i],"odd")
#     i=i+1



# list=[1,2,3,1,7,8,2,3,1,2,5,1,3]
# a=[]
# for i in list:
#     if i not in a:
#         a[i]=1
#     else:
#         a[i]=a[i]+1
# print(a)    



# a =[[1,2,3],[4,5,6,7],[8,9,10]]

# Loop over your list and print all elements that are of size 3
# for x in a:
    #   if len(x)==3:
        # print(x)
    # a=a+1


# a=[12,"34",5.1,8.1,19,"18",9.0]
# i=0
# n=[]
# while i<len(a):
#     if type(a[i])==float:
#         n.append(a[i])
#     else:
#         pass
#     i=i+1
# print(n)

# slicing

# a=["ram",20,"tanu",12.5]
# print(a)
# print(a[:1])
# print(a[3:])
# print(a[1:2])
# print(a[0:3])
# print(a[1:4])

# a=[10,20,-50,21.3,"amisha"]
# n=len(a)
# i=0
# while i<n:
#     print(i,a[i])
#     i=i+1

# ..change..

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)


# append-add

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)


# count()method

# fruits = ['apple', 'banana', 'cherry']
# x = fruits.count("cherry")
# print(x)


# a=[12,34,56,78,12,12,0,]
# b=a.count(12)
# print(b)

# i=0
# while i<10:
    # i=i+1
    # print(i)



# a = [1, 0, 0, 1, 1, 0, 1, 1]

# i=1
# c=0
# sum=0
# while i<=len(a):
#     b=a[-i]
#     sum+=(a[-i]*(2**c))
#     c=c+1
#     i=i+1
#     print(sum)



# txt = "welcome to the jungle"
# x = txt.split()
# print(x) 


# a="amishasharma"
# b= a.split()
# print(a)

# a=[4,8,7,2,5]

# i=0
# while i<len(a):
#     b=0
#     while b<len(a):
#         print(a[b],end=" ")
#     b=b+1
# print()    
#     i=i+1


# i=0
# while i<len(a):
#     c=0
#     while c<len(a):
#         print(c,end=" ")
#     c=c+1
#     i=i+1
# print(i)

# a=[10,9,8,7,6,5,4,3,2,1]

# i=10
# while i>=0:
#     i=i-1
#     print(i)


# txt = "hello  my name is Peter I am 26 years old"
# x = txt.split(" ")
# print(x)


# a= "amisha" "sharma"
# b=a.split(" ")
# print(a)

# a= "12 23 34 45 56 67 78 89 90"
# z=a.split(" ")
# print(z) 

# num=[4,8,7,2,5]

# a.reverse()
# print(a)
# i=len(num)-1
# while i >=0:
#     print(num[i])
#     i=i-1
# print(num[::-1])



#     j=0
#     while j<a[i]:
#         print(j)
#         j=j+1
#     i=i+1
# print(i)


# i = 0
# a = "Amisha sharma"
 
# while i < len(a):
#     if a[i] == 'e' or a[i] == 's':
#         i += 1
#         continue
         
#     print('Current Letter :', a[i])
#     i += 1


# a = "amisha sharma"
# a=[12,23,34,45,56,67,78,89,90]
# i = 0
 
# while i < len(a):
#     i += 1
#     pass
# print('Value of i :', i)



# list1 = [100, 200, 300, 400, 500]
# list1 = list1[::-1]
# print(list1)

# numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
# res = []
# for i in numbers:
    # calculate square and add to the result list
    # res.append(i * i)
# print(res)


# a= 1==True
# print(a)
# a= 0==False
# print(a)

# a=False==0
# print(a)

# a=10
# b=20
# c=a+b
# b=a+c
# print(a+b)

# a=10
# b=5
# c=b
# b=a
# a=c
# print(a)
# print(b)


# a=10
# b=5
# a,b=b,a
# b,a=a,b
# print(b)
# print(a)

# i=0
# while i<=10:
#     print(i)
#     i=i+1

# i=0
# while i<=10:
#     i=i+1
#     print(i)

# i=20
# while i>10:
#     print(i)
#     i=i-1

# x=int(input("enter the number"))
# if num<10:
#     print("10 se chota hai")
# else:
#     print("20 se bada hai")

# a=9
# b=5
# a=b
# b=a
# print(a+b)

# num="Megha"
# num3=3
# print(num,num3)


# a=int(input("Enter the number"))
# i=0
# while i<=10:
#     print(i,end=" ")
#     i=i+1
# i=0
# while i<=100:
#     if i%2==0:
#         print("+",i)
#     else:
#         print(-i)
#     i=i+1 

# i=0
# while i<=5:
#     print(str(i)*5)
#     i=i+1

# i=0
# while i<=10:
#     i=i+1
#     print(-i)

# a=int(input("Entre the number:"))
# i=0
# while i<=100:
#     if i%2==0:
#         print(i,"even")
#     else:
#         print(i,"odd")
#     i=i+1

# a=7
# b=(str(a))
# print(type(b))

# a=[21,23,34,54,65]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# a=int(input("Enter the number:-"))
# if a%2==0:
#     print("Even number")
# else:
#     print("Odd number")


# a="10.0"
# b=float(a)
# c=int(b)
# print(c)

# a=72
# b=float(a)
# print(b)

# a=1.5
# b=1.5
# print(a+b)

# x=5
# y=5
# print(x is y and y is x)

# print(True+true+False+false)

# print("s"+"A"+"W"+a)

# a="Ram"
# b=7
# c=7.5
# d=b+c
# f=str(a)
#e=d+a
# print(b+a)


# a=7
# b=(str(a))
# print(b)


a="amisha"
a+="sharma"
print(a)