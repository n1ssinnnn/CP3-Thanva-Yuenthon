num = int(input("Number : "))

for n in range(num):
    print(" "*(num-(n+1)) + "*"*((n*2)+1))