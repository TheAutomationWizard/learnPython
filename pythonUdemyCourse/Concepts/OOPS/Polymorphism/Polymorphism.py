from multipledispatch import dispatch


class Calculator:

    # ******************************************************
    #           Polymorphism - OverLoading Using Dispatcher
    # ******************************************************

    @dispatch(int, int)
    def product(self, first_input, second_input):
        return first_input * second_input

    @dispatch(int, int, int)
    def product(self, first_input, second_input, third_input):
        return first_input * second_input * third_input

    @dispatch(str, int)
    def product(self, input_string, multipier):
        return input_string * multipier

    def adding(self, integer1, integer2):
        print('Parent class Method.\nResult = ', integer1 + integer2)


# ******************************************************
#           Polymorphism - Overriding in Python
# ******************************************************

class Scientific_calculator(Calculator):

    def product(self, first_input, second_input):
        print('Scientific Calculator')
        return first_input * second_input

    def adding(self, integer1, integer2):
        print('Child class Method. Calling out super()')
        super().adding(integer1, integer2)


if __name__ == '__main__':
    calculate = Calculator()
    print(calculate.product(2, 3))
    print(calculate.product(2, 3, 5))
    print(calculate.product('*', 40))

    sCalc = Scientific_calculator()
    print(sCalc.product(2, 20))
    sCalc.adding(2,3)
