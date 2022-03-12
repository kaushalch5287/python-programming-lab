#to find prime number or not
n = int(input("enter the positive integer: "))
count = 0                   
for i in range(1,n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("prime number")
else:
    print("not prime number")
