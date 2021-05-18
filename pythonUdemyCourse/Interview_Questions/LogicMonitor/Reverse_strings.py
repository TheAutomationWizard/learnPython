"""
Available Concepts :
1) slicing
2) reversed keyword
3) join keyword
4) list comprehension
"""

"""
Reverse a string
"""


def string_reversal_one(*args):
    for input in args:
        print('Original \t : ', input, '\nReversed\t : ', input[::-1], '\n' + '*' * 40)


def string_reversal_two(*args):
    for test_string in args:
        output = ''
        for char in test_string:
            output = char + output
        print('Original \t : ', test_string, '\nReversed\t : ', output, '\n' + '*' * 40)


def string_reversal_three(string):
    if len(string) == 0:
        return string
    else:
        return string_reversal_three(string[1:]) + string[0]


def string_reversal_four(*args):
    for input in args:
        print('Original \t : ', input, '\nReversed\t : ', "".join(reversed(input)), '\n' + '*' * 40)


string1 = 'Test this string'
string2 = 'Aditya'
string3 = 'Reverse It'

string_reversal_one(string1, string2, string3)
string_reversal_two(string1, string2, string3)
print('\n', string_reversal_three(string1), '\n')
string_reversal_four(string1, string2, string3)

"""
 :: String Palindrome :: 
"""


def multiple_ways_to_check_palindrome(input):
    if input == input[::-1]:
        if input == "".join(reversed(input)):
            if input == "".join([last_Char for last_Char in reversed(input)]):
                temp = ""
                if input == "".join([last_Char + temp for last_Char in input]):
                    print('Yes a Palindrome')
                    return
                else:
                    print('Failed Method 3')
            else:
                print('Failed Method 2')
        else:
            print('Failed Method 1')
    print('Not a Palindrome')


multiple_ways_to_check_palindrome('abccba')
multiple_ways_to_check_palindrome('abccbao')


def integer_palindrome(*args):
    for integer_number in args:
        temp = 0
        copy_number = integer_number
        for counter in range(0, len(str(integer_number))):
            temp = 10 * temp +  copy_number % 10
            copy_number = int(copy_number / 10)
        if integer_number == temp:
            print(f'{integer_number} is a palindrome.')
        else:
            print(f'{integer_number} is not a palindrome.')


integer_palindrome(121, 1001, 1001, 110, 1010, 1221)
