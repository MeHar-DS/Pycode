# small anonymous functions can be created by lambda keyword
# lambda functions is used wherever function objects are required


def incrementor(n):
    return lambda x:x+n

f = incrementor(1)
print(f(5))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
