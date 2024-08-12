num = int(input("Enter any number:"))

for i in range(num):
    if num % 1 == 0 and num % num == 0:
        print(f"{num } is a prime number")
        break

    else:
        print(f"{num } is a composite number")