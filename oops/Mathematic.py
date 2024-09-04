class Mathematics:
        def __init__(self, first_number, second_number):
            self.a = first_number
            self.b = second_number
        
        def sum(self):
            print("addition is: ", self.a + self.b)
        def sub(self):
            print("subtraction is: ", self.a - self.b)
        def mul(self):
            print("product is: ", self.a * self.b)

a = int(input("Enter any number: "))
b = int(input("Enter any number: "))

obj = Mathematics(a, b)

obj.sum()
obj.sub()
obj.mul()
        