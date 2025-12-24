#pattern of square
x=int(input())
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print()

#pattern of triangle
x=int(input())
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")

#pattern of numbers
x=int(input())
for i in range(x):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")

#pattern of pyramidal 
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

#pattern of diamond
x=int(input())
for i in range(x):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(x-2,-1,-1):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

