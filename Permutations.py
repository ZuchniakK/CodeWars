from itertools import permutations as perm


def permutations(string):
    return [''.join(i) for i in perm(string)]


if __name__ == '__main__':
    print(permutations('abc'))
