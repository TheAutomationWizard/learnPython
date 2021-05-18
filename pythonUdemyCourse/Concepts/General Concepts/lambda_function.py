"""
Lambda Method : An anonymous function is known as a lambda function. This function can have any number of parameters but,
 can have just one statement.

Other Topics :
1) List Comprehension
2) Generators
"""


def calculate_squares(*args):
    for number in args:
        print(number ** 2)


my_square_lambda = lambda *args: [squared ** 2 for squared in args]
my_square_lambda_generator = lambda *args: [(yield squared ** 2) for squared in args]

my_list = list(range(10, 40, 3))

print('*' * 40)
calculate_squares(*my_list)
print('*' * 40)
print(*my_square_lambda(*my_list))
print('*' * 40)
print(*my_square_lambda_generator(*my_list))

# ******************************************************************

"""
High Order Functions :
"""

high_order_lambda = lambda var, sample_func: var + sample_func(var)
print(high_order_lambda(2, lambda var_: var_ ** 2))

"""
IIFE _ Immediately invoked function execution
"""
print('*' * 40)
print((lambda x, y: x ** y)(2, 3))


