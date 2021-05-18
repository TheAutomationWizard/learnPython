def check_even_odd(num1):
    return num1 % 2 == 0


def first_method(num1, num2):
    if check_even_odd(num1) and check_even_odd(num2):
        return min(num1, num2)
    return max(num1, num2)


print(first_method(2, 4))
print(first_method(2, 5))


# ****************************************************
# ****************************************************


def two_word_string(input):
    w1, w2 = input.lower().split()
    return w1[0] == w2[0]


print(two_word_string('Levadsafdsf Lagdsfsd'))
print(two_word_string('Crazy Kangaroo'))


# ****************************************************
# ****************************************************


def other_side_of_seven(num1):
    if num1 < 7:
        return (7 - num1) * 2 + 7
    else:
        return 7 - (num1 - 7) * 2


print(other_side_of_seven(4))
print(other_side_of_seven(12))


# ****************************************************
# ****************************************************


def cap_first_and_fourth_letter(input):
    return input[:3].capitalize() + input[3:].capitalize()


print(cap_first_and_fourth_letter('macdonald'))


# ****************************************************
# ****************************************************

def descend_the_words(input):
    output = ''
    for words in input.split():
        output = words + ' ' + output
    return output


print(descend_the_words('I am home'))
print(descend_the_words('We are ready'))


# ****************************************************
# ****************************************************

def almost_there_number(num):
    if num in range(90, 111) or num in range(190, 211):
        return True
    return False


def almost_there_number_using_abs(num):
    return abs(num - 100) <= 10 or abs(num - 200) <= 10


print(almost_there_number(90))
print(almost_there_number(104))
print(almost_there_number(150))
print(almost_there_number(109))

print('*' * 40)
print(almost_there_number_using_abs(90))
print(almost_there_number_using_abs(104))
print(almost_there_number_using_abs(150))
print(almost_there_number_using_abs(109))


# ****************************************************
# ****************************************************

def actual_pattern_counter(input, pattern):
    counter = 0
    for index, character in enumerate(input):
        if pattern[0] == character:
            if input[index:index + len(pattern)] == pattern:
                counter += 1
        continue
    return counter


print(f"Pattern 'hah' in 'hahahah' occured {actual_pattern_counter('hahahah', 'hah')} times")


# ****************************************************
# ****************************************************

def return_thrice_characters(input):
    output = ''
    for word in input:
        output += word * 3
    return output


print(return_thrice_characters('hello'))


# ****************************************************
# ****************************************************


def blackjack(num1, num2, num3):
    total = num1 + num2 + num3
    if total <= 21:
        return total
    elif total <= 31 and 11 in (num1, num2, num3):
        return total - 10
    return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# ****************************************************
# ****************************************************

def summer_of_69(args):
    toggle = False
    summation = 0
    for num in args:
        if num == 6 and not toggle:
            toggle = True
        if num != 6 and not toggle:
            summation += num
            continue
        if num == 9 and toggle:
            toggle = False

    return summation


print(summer_of_69([1, 3, 5]))
print(summer_of_69([4, 5, 6, 7, 8, 9]))
print(summer_of_69([2, 1, 6, 9, 11]))


# ****************************************************
# ****************************************************


def james_bond(agent_codes):
    expected = [0, 0, 7]
    for code in agent_codes:
        if code == expected[0]:
            expected.remove(code)
            if len(expected) == 0:
                return True
    return False


print(james_bond([1, 2, 4, 0, 0, 7, 5]))
print(james_bond([1, 0, 2, 4, 0, 5, 7]))
print(james_bond([1, 7, 2, 0, 4, 5, 0]))


# ****************************************************
# ****************************************************

def prime_counter(upper_limit):
    count = 0
    flag = False
    for num in range(2, upper_limit + 1):
        for check in range(2, int((num / 2)) + 1):
            if (num % check) == 0:
                flag = True

        if flag:
            flag = False
        else:
            count += 1

    return count


print(prime_counter(100))
