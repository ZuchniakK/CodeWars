from time import time
from random import randint


def find_most_frequent(l):
    most_frequent = filter(lambda x: l.count(x) == l.count(max(set(l), key=l.count)), set(l))
    return set(list(most_frequent))


def find_most_frequent2(l):
    return set(x for x in set(l) if l.count(x) == max([l.count(y) for y in l]))


if __name__ == '__main__':
    l = [1, 2, 3, 3, 4, 5, 5, 6, '2', '2']
    print(find_most_frequent(l))
    k = 10
    l = [randint(0, 100) for i in range(k)]
    n = 100
    start = time()
    for i in range(n):
        find_most_frequent(l)
    print('My solution ', time() - start)

    start = time()
    for i in range(n):
        find_most_frequent2(l)
    print('Best CodeWars solution', time() - start)
