"""
Decorators :
"""


# Idea behind decorators , working of decorators

def generate_square(var1):
    print(var1 ** 2)
    return var1 ** 2


# Lets use above function to generate sqaures of squares i.e raised to power 4

def generate_power_4(function, x):
    def sqauring_again():
        print(f'{x} ^ 4 = ', function(x ** 2))

    return sqauring_again


# generate_square(2)
power4 = generate_power_4(generate_square, 2)
power4()

# The above method generate_power_4 is being used to decorate generate_square to get power ^ 4 as output.
print('\n\n', '*' * 40)


def decorator_to_add_extra_functionality(func):
    print(f'decorating Function : {func.__name__}')

    def gen_quad(*args, **kwargs):
        return [func(arg ** 2) for arg in args]

    return gen_quad


@decorator_to_add_extra_functionality
def squaring_input(input):
    print(f'squaring {input}')
    return input ** 2


x = squaring_input(3)
print(*squaring_input(2, 5))
print(*squaring_input(4))

"""
Generators : 

"""
