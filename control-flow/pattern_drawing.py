size = int(input("Enter the size of the pattern: "))
while size >= 1 :
    for i in range(size,1) :
        print("*", end="")
        size-=1