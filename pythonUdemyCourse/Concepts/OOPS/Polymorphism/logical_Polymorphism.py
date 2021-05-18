class show_polymorphism:

    def polymorphic_area_calculator(self, height=None, length=None):
        if height and length is not None:
            return f'Area of Rectangle = {height * length}'
        elif height is not None:
            return f'Area of Square = {height * height}'
        else:
            return 'Enter valid dimensions to calculate area.'


obj = show_polymorphism()
print(obj.polymorphic_area_calculator(2))
print(obj.polymorphic_area_calculator(2, 3))
