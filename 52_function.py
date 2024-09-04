def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

input_num = int(input("Enter a number: "))
if isPrime(input_num):
    print(f"{input_num} is a prime number.")
else:
    print(f"{input_num} is not a prime number.")



#revise from function