import string
from math import pi

volume = lambda radius: (4 / 3) * pi * (radius ** 3)

print(volume(2))


# ************************************************
# ************************************************

def range_chk(num, low, high):
    if num in range(low, high + 1):
        return f'{num} is in the range between {low} and {high}'
    else:
        return f"{num} isn't in the range between {low} and {high}"


print(range_chk(5, 2, 7))

range_check = lambda num, low, high: num in range(low, high + 1)

print(range_check(3, 1, 10))


# ************************************************
# ************************************************


def case_counter(input_string):
    lowercase_count = 0
    uppercase_count = 0
    for alphabet in input_string:
        if alphabet.isalpha():
            if alphabet.isupper():
                uppercase_count += 1
            else:
                lowercase_count += 1
    print(f"No. of Upper case characters : {uppercase_count}")
    print(f"No. of Upper case characters : {lowercase_count}")


case_counter('Hello Mr. Rogers, how are you this fine Tuesday?')


# ************************************************
# ************************************************

def remove_duplicates(list_):
    unique_list = []
    for item in list_:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)
    return unique_list


remove_duplicates([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])

rem_dupli = lambda list_: set(list_)

print(rem_dupli([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


# ************************************************
# ************************************************

def multiply(list_):
    product = 1
    for item in list_:
        product *= item
    print(product)


multiply([1, 2, 3, -4])

# ************************************************
# ************************************************

print(list(map(lambda input_: input_.replace(' ', '') == input_[::-1].replace(' ', ''), ['hell eh'])))

# ************************************************
# ************************************************

pangram_checker = lambda input: len(set(input.replace(' ', '').lower())) == 26

print(pangram_checker('The quick brown fox jumps over the lazy dog'))


# ************************************************
# ************************************************


