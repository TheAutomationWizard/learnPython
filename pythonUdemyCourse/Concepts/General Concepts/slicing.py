list = [1, 2, 34, 4, 56, 7, 8, 99, 2]


def various_slicing_in_python(list_object):
    """
    slicing operations in python
    :param list_object:
    :return:

    slice (Start, end , step)
    """
    # Using slice method
    print(list_object[slice(0, 4, 1)])
    # Using index slicing  +==>  [start : stop+1 : steps]
    # Step sign(+ or -), must be sign of stop+1 -start
    print(list_object[::-1])

    # Negative Indexing to slice
    print(list_object[-1:-4:-1])
    

if __name__ == '__main__':
    various_slicing_in_python(list)
