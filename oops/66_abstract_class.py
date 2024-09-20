from abc import ABC, abstractmethod

# class Polygon(ABC):
#     @abstractmethod
#     def noofsides(self):
#          print("This is not made in a proper way")

#     def area(self):
#         print("this is the area of triangle")


# class Triangle(Polygon):
#     def noofsides(self):
#         print("I have 3 sides")
            

# triangle_pbj = Triangle()
# triangle_pbj.area() 
# triangle_pbj.noofsides()


class Shape:
    def area_of_triangle(self, b, h):
        return 0.5 * b * h
    def area_of_rectangle(self, l, w):
        return l * w
    @abstractmethod
    def area_of_square(self, l):
        return l * l
    