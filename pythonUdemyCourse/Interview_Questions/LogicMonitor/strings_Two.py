"""
Program : String Pattern
i/p = Abcd
o/p = a-bb-ccc-dddd
"""


def changePattern(input):
    counter = 1
    output = ""
    for char in input:
        output += (char.lower() * (counter))
        if counter != len(input):
            output += '-'
        counter += 1
    print(output)


changePattern('Abcd')

"""
Program : Valid Paranthese
Input : [({})], [[)(]]
Output : valid, invalid
"""


def valid_parentheses(input):
    stack = []

    for parentheses in input:
        if parentheses in ['{', '[', '(']:
            stack.append(parentheses)

        else:
            if not stack:
                print(input, ' +==> Contains Invalid parentheses.')
                return
            else:
                top = stack[-1]
                if parentheses == ']' and top == '[' or \
                        parentheses == '}' and top == '{' or \
                        parentheses == ')' and top == '(':
                    stack.pop()

    if not stack:
        print(input, ' +==> Contains Valid Parentheses.')
    else:
        print(input, ' +==> Contains Invalid parentheses.')


valid_parentheses("{{}}()[()]")
valid_parentheses("{][}")
valid_parentheses(")")
valid_parentheses("()(")
