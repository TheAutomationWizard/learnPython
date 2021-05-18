sentence = 'Print only words that starts with s in a sentence'

for word in sentence.split():
    if word.startswith('s'):
        print(word)

print('*' * 100)

print(list(word for word in sentence.split() if word.startswith('s')))

print('*' * 100)

for number in range(0, 11):
    if number % 2 == 0:
        print(number)

for number in range(0,11, 2):
    print(number)

print('*' * 100)

print([number for number in range(0, 11) if number % 2 == 0])

print('*' * 100)

print([number for number in range(1, 51) if number % 3 == 0])

print('*' * 100)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word)

print('*' * 100)

print([word for word in st.split() if len(word) % 2 == 0])

print('*' * 100)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('BuzzFizz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)

print('*' * 100)

st = 'Create a list of the first letter of every word in this string'
my_list = [letter[0] for letter in st.split()]
print(my_list)

print('*' * 100)
