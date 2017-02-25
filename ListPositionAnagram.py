from string import ascii_uppercase
from functools import reduce
from collections import Counter
from time import time


def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset + 1)
        except ValueError:
            return result
        result.append(offset)


def permutation_number(set, remove_element=-1):
    print('permutation', set, 'delete', remove_element)
    denominator = 0
    divider = 1
    for i in set:
        tmp = i[2]
        if i[1] == remove_element: tmp -= 1
        print('-', i[0], i[1], tmp)
        if tmp > 0:
            denominator += tmp
            divider *= reduce(lambda x, y: x * y, range(1, tmp + 1))

    permutation = reduce(lambda x, y: x * y, range(1, denominator + 1)) // divider
    print('permutation', permutation)
    return permutation


def list_position(word):
    chars = list((map(lambda i: (i, ascii_uppercase.index(i), word.count(i)), word)))

    print(chars)
    set_chars = list(set(chars))
    chars = [[char[0], char[1], char[2]] for char in chars]
    set_chars = [[char[0], char[1], char[2]] for char in set_chars]
    sorted_chars = sorted(chars)
    position = 1
    for char in chars:
        k = sorted_chars.index(char)
        print(chars, char, 'index', sorted_chars.index(char))
        print(sorted_chars)
        sorted_index = -1
        for sorted_char in sorted_chars[:k]:
            if sorted_index != sorted_chars.index(sorted_char):
                print(sorted_char)
                position += permutation_number(set_chars, remove_element=sorted_char[1])
                print(" ")
            sorted_index = sorted_chars.index(sorted_char)
        sorted_chars.remove(char)

        set_chars[set_chars.index(char)][2] -= 1
        for index in indices(chars, char):
            chars[index][2] -= 1
    return position


def list_position2(word):
    l, r, s = len(word), 1, 1
    c = Counter()

    for i in range(l):
        x = word[(l - 1) - i]
        c[x] += 1
        print(c)
        for y in c:
            print(y, x, y < x)
            if y < x:
                r += s * c[y] // c[x]
        s = s * (i + 1) // c[x]
    return r


if __name__ == '__main__':
    word = 'BHGBY'
    start = time()
    print(list_position2(word))
    print(time() - start)
