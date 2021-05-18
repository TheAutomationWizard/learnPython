import random


def gensqures(N):
    for num_to_square in range(N + 1):
        yield num_to_square ** 2


for squared_number in gensqures(10):
    print(squared_number)

print('*' * 50 + '\n')


def random_number_generator(low, high, n):
    for req_numbers in range(n):
        yield random.randint(low, high)


for randomInteger in random_number_generator(1, 10, 12):
    print(randomInteger)

s = 'hello'
s_iter = iter(s)
print(next(s_iter))


# Generator Comprehension
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
