def get_first_non_repetitive_Case_sensitive(input):
    position_holder = 0
    unique_flag = False
    for character in input:
        position_holder += 1
        sub_position_holder = 0
        for other_char in input.lower():
            sub_position_holder += 1
            if position_holder == sub_position_holder:
                continue
            if other_char == character.lower():
                unique_flag = False
                break
            unique_flag = True

        if unique_flag:
            return character
    return ""


print(get_first_non_repetitive_Case_sensitive('sTress'))
print(get_first_non_repetitive_Case_sensitive('srress'))
print(get_first_non_repetitive_Case_sensitive('srrEess'))
print(get_first_non_repetitive_Case_sensitive('srrEessX'))





def cyclic_sub_string(input):
    counter = 0
    while input[:counter + 1] in input[counter + 1:]:
        counter += 1
        if not input[:counter + 1] in input[counter + 1 :]:
            if ((input + input[counter:])[len(input[counter:]):]) == input:
                return len(input[counter:])
    return len(input)


print('cyclic length : ', cyclic_sub_string('cabca')) # 3
print('cyclic length : ', cyclic_sub_string('caabcaa')) # 4
print('cyclic length : ', cyclic_sub_string('ccabocca')) # 5
print('cyclic length : ', cyclic_sub_string('aabbox')) # 6
