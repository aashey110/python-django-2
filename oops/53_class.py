class Calculator():
    
    def sum(self, num1, num2):
        add = num1 + num2
        print(f"{num1} + {num2} = {add}")

    def difference(self, num1, num2):
        subtract = num1 - num2
        print(f"{num1} - {num2} = {subtract}")

    def product(self, num1, num2):
        mulitply = num1 * num2
        print(f"{num1} * {num2} = {mulitply}")

    def quotient(self, num1, num2):
        divide = num1 / num2
        print(f"{num1} / {num2} = {divide}")

cal = Calculator()

num1 = int(input("Ener any number: "))
num2 = int(input("Ener any number: "))

cal.sum(num1, num2)

cal.difference(num1, num2)

cal.product(num1, num2)

cal.quotient(num1, num2)