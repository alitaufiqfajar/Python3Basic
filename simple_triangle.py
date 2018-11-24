x = int(input("Please enter your number: "))
temp = x

for i in range(0, x):
    temp-=1
    print((' '*temp)+('* '*i))
