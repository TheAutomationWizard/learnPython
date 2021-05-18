class A(object):
    def __init__(self, a, *args, **kwargs):
        print('I (A) am called from B super()')
        print("A", a)


class B(A):
    def __init__(self, b, *args, **kwargs):
        print('As per inverted flow, i am called from class A1 super()')
        super(B, self).__init__(*args, **kwargs)
        print("B", b)


class A1(A):
    def __init__(self, a1, *args, **kwargs):
        print('A1 super will call, B super now! But without positional parameter "b" in super()')
        super(A1, self).__init__(*args, **kwargs)
        print("A1", a1)


class B1(A1, B):
    def __init__(self, b1, *args, **kwargs):
        super(B1, self).__init__(*args, **kwargs)
        print("B1", b1)


B1(a1=6, b1=5, b="hello", a=None)


# *************************************
#   Understand flow of kwargs & args
# *************************************

def ab(x, a=10, a1=20, **kwargs):
    print(f'Value of x : {x}')
    print(f'Value of a : {a}')
    print(f'Value of a1 : {a1}')
    print('value of kwargs')
    print(kwargs)


kwarg_dict = {'x': 200, 'a': 50, 'a1': 100, 'b': 1000, 'c': 101}
ab(**kwarg_dict)
