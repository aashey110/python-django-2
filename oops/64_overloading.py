class Mathematics:
    def add(self, a, b):
        print(a + b)

    def sub(self, a, b):
        print(a - b)
    
    def mul(self, a, b, c = 1):
        print(a * b * c)


class Overriding(Mathematics):
    def add(self, a, b, c=0):
        print(a + b)
        
    def sub(self, a, b):
        print(a - b)
    
    def mul(self, a, b, c = 1):
        print(a * b * c)

overriding_obj = Overriding()

overriding_obj.add(10,20,20)
overriding_obj.sub(20,10)
overriding_obj.mul(1,2,5)

