class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius= radius
    def get_area(self):
        return Circle.pi * self.radius * self.radius
    def get_circumference (self):
        return 2*Circle.pi * self.radius
circle_1 = Circle (4)
print(f'The area of circle 1 is {circle_1.get_area()}')
print (f'The circumference of circle_1 is: {circle_1.get_circumference()}')