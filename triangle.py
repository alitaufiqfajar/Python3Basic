x = int(input("Please enter your number: "))
temp = x
for i in range(0, x): 
    for j in range(0, temp): 
        print(" ",end="")
    temp-=1
    for k in range(0,i+1):
        print("* ", end="")
    print("")
