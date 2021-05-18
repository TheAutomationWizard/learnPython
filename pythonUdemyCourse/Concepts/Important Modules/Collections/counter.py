from collections import Counter

list_ = [1, 23, 4, 5, 6, 1234, 1, 23, 1, 2, 2, 2, 4, 3, 7, 9, 3]
cnt = Counter()

cnt.update('asdfsadfadsdfsdb')
print(cnt)

cnt.update({'a' : 10, 'b':-2})
print(cnt)

print(cnt[1])
print(cnt['a'])


# Most Common Methods in counter

print(*cnt.elements())

print(*cnt.most_common())