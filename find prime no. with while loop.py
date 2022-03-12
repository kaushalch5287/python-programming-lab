#with while loop to find prime no.

n = int(input("enter the number: "))
while n%n == 0:
    print("prime")
    break 
else:
    print("not prime")
