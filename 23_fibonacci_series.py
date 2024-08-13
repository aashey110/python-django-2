num1 = 1
num2 = 1
print(f"{num1} \n{num2}")

temp = 0

for i in range(10):
    temp = num1 + num2
    num1 = num2
    num2 = temp
    print(temp)