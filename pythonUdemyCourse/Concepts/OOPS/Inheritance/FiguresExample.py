class Quadrilateral:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def quad_area(self):
        area_ = self.length * self.height
        print(f'Area of Quadrilateral with length {self.length} and height : {self.height} is = {area_}')
        return area_


class Square(Quadrilateral):
    def __init__(self, length):
        super().__init__(length, length)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_ = 3.14 * self.radius * self.radius
        print(f'Area of circle with radius {self.radius} is = {area_}')
        return area_


class Cylinder(Circle, Square):
    def __init__(self, radius, height , *args, **kwargs):
        self.radius = radius
        self.height = height

    def area(self):
        base_area1 = super().area() * 2
        base_length = 3.14 * self.radius * 2 * self.height
        self.length = self.radius
        quad_area = super().quad_area()
        return base_area1 + base_length


radius = 2
height = 5
myCylinder = Cylinder(radius=radius, height=height)
print(myCylinder.area())

# print(2 * 3.14 * radius * (radius + height))
# print(2 * 3.14 * radius * height)
