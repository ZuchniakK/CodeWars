def recover_secret(triplets):
    chars = []
    [list.extend(chars, i) for i in triplets]
    chars = list(set(chars))
    rules = []
    for triplet in triplets:
        rules.append([triplet[0], triplet[1]])
        rules.append([triplet[0], triplet[2]])
        rules.append([triplet[1], triplet[2]])
    is_change = True
    while is_change:
        is_change = False
        for rule in rules:
            i = chars.index(rule[0])
            j = chars.index(rule[1])
            # print(rule, i, j)
            if i > j:
                chars[i], chars[j] = chars[j], chars[i]
                is_change = True
    return "".join(chars)


if __name__ == '__main__':
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]
    secret = recover_secret(triplets)
    print(secret)
