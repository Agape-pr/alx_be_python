import math
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError

    


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

        super().__init__()
        
    def area(self):
       return self.length * self.width

class circle(Shape):
     def __init__(self, radius):
          self.radius = radius
          super().__init__()
     def area(self):
         return self.radius * self.radius * math.pi
        
