

n = input("Enter First Number: ")
m = input("Enter Second Number: ")

prime_numbers = []
def prime_check(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


for i in range(int(n), int(m)+1):
        if i < 2:
             pass
        else:
            check = prime_check(i)
            if check == True:
                prime_numbers.append(i)
print(f"Total Prime Numbers between {n} and {m}")
print(prime_numbers)
print("Sum of Prime Numbers: ", sum(prime_numbers))