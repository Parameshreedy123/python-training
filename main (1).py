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
