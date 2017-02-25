def next_bigger(n):
    lis = [int(i) for i in str(n)]
    for i in range(len(lis) - 1, 0, -1):
        if lis[i] > lis[i - 1]:
            l = lis[i - 1:].index(min(list(filter(lambda x: x > lis[i - 1], lis[i:]))))
            lis[i - 1], lis[l + i - 1] = lis[l + i - 1], lis[i - 1]
            lis_f = lis[:i]
            lis_f.extend(sorted(lis[i:]))
            return int("".join(map(str, lis_f, )))
    return -1


if __name__ == '__main__':
    dig = 144
    print(dig)
    k = next_bigger(dig)
    print(k)

    my_list = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
    k = list.index(my_list[3:], 2)
    print(k + 3)
