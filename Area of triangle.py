class Triangle:
    formula =0.5 #Class attribute
    def __init__(self, base, height):
        self.base= base
        self.height= height
    def area(self):
        return (self.formula*self.base*self.height)
triangle_1 = Triangle (10, 20)
triangle_1.area()
print(triangle_1.area())