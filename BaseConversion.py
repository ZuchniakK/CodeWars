bin = '01'
oct = '01234567'
dec = '0123456789'
five = '01234'
hex = '0123456789abcdef'
allow = 'abcdefghijklmnopqrstuvwxyz'
allup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(input, source, target):
    input_base, output_base = len(source), len(target)
    print(input_base, output_base)
    value = sum([source.index(input[-i - 1]) * input_base ** i for i in range(len(input))])
    print(value)
    output = []
    i = 0
    while True:
        if value >= output_base ** i:
            output.append([])
            i += 1
            continue
        break
    if len(output) == 0:
        output.append([])
    print(output)
    for i in range(len(output)):
        output[i] = target[value // output_base ** (len(output) - i - 1)]
        value %= output_base ** (len(output) - i - 1)
    print(output)
    return ''.join(output)


if __name__ == "__main__":
    print(convert('0', dec, alpha))
    print(convert('154', dec, alpha))
    print(convert('154', dec, hex))
    print(convert('154', dec, alphanum))
    print(convert('ddfgdfggdf', allow, alphanum))
