# import time
# from TotalTime import fn_timer
import sys
import signal

sys.setrecursionlimit(10000000)
signal.signal(signal.SIGSEGV, signal.SIG_IGN)


def fib1(n):
    if isinstance(n, int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            return fib1(n - 1) + fib1(n - 2)
        else:
            return
    else:
        return -1


# @fn_timer
def fib2(n):
    x, y = 0, 1
    while n:
        x, y, n = y, x + y, n - 1
    return x


# @fn_timer
def fib3(n):
    def fib_iter(a, x, y):
        if a == 0:
            return x
        else:
            return fib_iter(a - 1, y, x + y)

    return fib_iter(n, 0, 1)

known = {0: 0, 1: 1}


def fib4(n):
    if n in known:
        return known[n]
    res = fib4(n - 1) + fib4(n - 2)
    known[n] = res
    return res


known_list = [0, 1]


def fib5(n):
    if len(known_list) > n:
        return known_list[n]
    res = fib5(n - 1) + fib5(n - 2)
    known_list.append(res)
    return res


def fib6(n):
    fibs = [0, 1]
    for i in range(n):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs[n]


if __name__ == '__main__':
    # start = time.clock()
    z = input("num=")
    for zz in range(z):
        fib4(zz)
    print fib4(z)
    # end = time.clock()
    # print('Running time: %s Seconds' % (end - start))
