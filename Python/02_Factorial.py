
n = int(input("Enter Number: "))

if n == 0:
    print(f"Factorial of :{n}=",1)
elif n < 0:
    print("Number Error")
else:
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    print(f"Factorial of {n} is =", sum)