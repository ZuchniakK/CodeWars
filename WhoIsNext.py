def who_is_next(names, r):
    names_len = len(names)

    full_round = 0
    pos = 0
    while r > pos:
        pos += names_len * 2 ** full_round
        full_round += 1
    pos -= names_len * 2 ** (full_round - 1)
    counter = 1
    queue = r - pos
    while queue > 0:
        queue -= 2 ** (full_round - 1)
        counter += 1

    return names[counter - 2]


if __name__ == '__main__':
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    for i in range(1000):
        print(i + 1, whoIsNext(names, i + 1))
