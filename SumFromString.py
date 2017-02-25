import re


def sum_from_string(string):
    digit_list = []
    digit_list.append([])
    for i in string:
        if i.isdigit(): pass
    digit_sum = re.findall(r'\d+', string)
    return sum(list((map(int, digit_sum))))


if __name__ == '__main__':
    string = "In 2015, I want to know how 23.5much does iPhone 6+ cost?"
    print(sum_from_string(string))
