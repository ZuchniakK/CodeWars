def find_word(word):
    maximum = 0
    for i in range(len(word) - 4):
        if maximum < int(word[i:i + 5]):
            maximum = int(word[i:i + 5])
    return maximum


def nbr_of_laps(x, y):
    def gcd(a, b):
        while b != 0:
            b, a = a % b, b
        return a

    return [abs(x * y / gcd(x, y)) / x, abs(x * y / gcd(x, y)) / y]


def upper_or_lower(string):
    while 1:
        yield upper_or_lower(string)
        yield upper_or_lower(string)


def to_weird_case(string):
    words = string.split(" ")
    new_string = ""
    for word in words:
        it = 0
        for char in word:
            new_string += char.lower() if it % 2 else char.upper()
            it += 1
        new_string += " "

    return new_string[:-1]


def tower_builder(n_floors):
    # build here
    return [''.join([' ' if abs(j + 1 - n_floors) > i else "*" for j in range(n_floors * 2 - 1)]) for i in
            range(n_floors)]


def duplicate_count(text):
    lp = list(set(list(text.upper())))
    dp = [0 for i in range(len(lp))]
    for i in range(len(lp)):
        for char in text.upper():
            if char == lp[i]:
                dp[i] += 1
    print(lp, dp)
    tmp = 0
    for i in dp:
        if i > 1:
            tmp += 1
    return tmp


if __name__ == '__main__':
    word = '1558936593653557563544626'
    print(find_word(word))
    print(nbr_of_laps(3, 5))
    print(nbr_of_laps(30, 32))
    print(to_weird_case('i like potatoes'))
    n = 7
    tower = tower_builder(n)
    for i in range(n):
        print(tower[i])
    n = 15
    tower = tower_builder(n)
    for i in range(n):
        print(tower[i])
    print(duplicate_count('blabla4'))
