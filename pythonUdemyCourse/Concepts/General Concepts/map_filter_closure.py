def sqaure_my_num(input):
    return input ** 2


my_list = list(range(7, 25, 4))

# Using Loops
for item in my_list:
    print(sqaure_my_num(item))

"""
Maps : 
"""
# Using Map
print(*map(sqaure_my_num, my_list))
# Map on lambda
print(*map(lambda x: x ** 2, my_list))

"""
Filters : A filter usually works with set of data, and a function that returns either of True/False.

filter (function, iterable )  
    => function => can be any function that returns True or false.  *********  ( Example 1) *********
                    ********* ( Example 2 ) **********
                => can be "None", in which case it defaults to Identity Function and check for non true values in the iterable.
                => Non - true values => 0 , False. Note 0 in string i.e. '0' doesn't corresponds ot False.
                => True values = anything but 0 or False.
"""

# Filter to find even numbers

print(*filter(lambda x: x % 2 == 0, list(range(0, 10))))
print(*filter(None, [0, 1, 2, False, True, '0', 'False']))

"""
Closures : A closure is a function where every free variable, everything except parameters,
 used in that function is bound to a specific value defined in the enclosing scope of that function.
  In effect, closures define the environment in which they run, and so can be called from anywhere.
"""


def enclosing_function(var1):
    var2 = 2

    def closure_func(var3):
        print(f"X : {var1}, Y : {var2} , Z : {var3}")
        return var1 + var2 + var3

    return closure_func


print('\n\n', '*' * 40)
for integer in range(3):
    closure = enclosing_function(integer)
    print(f"Closure({2 + integer}) = {closure(2 + integer)}")
