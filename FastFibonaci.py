from numpy import matrix


def fibonacci_n(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return fiboo(n)[0]


def fib(n):
    if n < 0: return (-1) ** (n % 2 + 1) * fib(-n)
    a = b = x = 1
    c = y = 0
    while n:
        if n % 2 == 0:
            (a, b, c) = (a * a + b * b,
                         a * b + b * c,
                         b * b + c * c)
            n /= 2
        else:
            (x, y) = (a * x + b * y,
                      b * x + c * y)
            n -= 1
    return y


def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return fiboo(n)[0]


def fiboo(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fiboo(n // 2)
        if n % 2 == 0:
            return a * (b * 2 - a), a * a + b * b
        else:
            # if n = 2k + 1 return (fib(2k +1), fib(2k + 2))
            return a * a + b * b, a * a + b * b + a * (b * 2 - a)


def slow_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(n):
        tmp = a
        a = b
        b = tmp + b
    return b


def fib_matrix(n):
    return (matrix(
        '0 1; 1 1' if n >= 0 else '-1 1; 1 0', object
    ) ** abs(n))[0, 1]


def with_else(k):
    if k % 2 == 0:
        return 0
    else:
        return 1


def with_out_else(k):
    if k % 2 == 0:
        return 0
    else:
        return 1


if __name__ == '__main__':

    n = 1000000
    from time import time

    start = time()
    k = fibonacci(n)
    # print(k)
    print("My solution", time() - start)

    start = time()
    k = fibonacci_n(n)
    # print(k)
    print("Nayuki solution", time() - start)

    start = time()
    k = fib(n)
    # print(k)
    print("Best CodeWars solution", time() - start)

    start = time()
    k = fib_matrix(n)
    # print(k)
    print("matrix code wars", time() - start)

    n = 1000000
    start = time()
    for i in range(n):
        with_else(1)
    print("with else ", time() - start)

    start = time()
    for i in range(n):
        with_out_else(1)
    print("without else ", time() - start)
    n = 1000
    start = time()
    for i in range(n):
        i ** 2
    print("using pow i**2", time() - start)

    start = time()
    for i in range(n):
        i * i
    print("using multiplication i*i", time() - start)

    n = 3000
    start = time()
    for i in range(n):
        for j in range(n):
            i * (i + j)
    print("using () i*(i+j)", time() - start)

    start = time()
    for i in range(n):
        for j in range(n):
            i * i + i * j
    print("without () i*i+ i*j", time() - start)
