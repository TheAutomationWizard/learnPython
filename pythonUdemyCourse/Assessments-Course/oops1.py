print('\n\n' + '*' * 50 + '\n')


class Line:
    def __init__(self, coord1, coord2):
        self.coordinate1 = coord1
        self.coordinate2 = coord2
        self.x1, self.y1 = self.coordinate1
        self.x2, self.y2 = self.coordinate2

    def distance(self):
        x_dist = (self.x1 - self.x2) ** 2
        y_dist = (self.y1 - self.y2) ** 2
        return (x_dist + y_dist) ** 0.5

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)


coord1 = (3, 2)
coord2 = (8, 10)
my_line = Line(coord1, coord2)
print(my_line.distance())
print(my_line.slope())


class Cylinder:
    def __init__(self, height, radius):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * 3.14 * self.radius * (self.height + self.radius)


my_cylinder = Cylinder(2, 3)
print(my_cylinder.volume())
print(my_cylinder.surface_area())