from TotalTime import fn_timer
import sys

sys.setrecursionlimit(1000000)


@fn_timer
def fib3(n):
    def fib_iter(a, x, y):
        if a == 0:
            return x
        else:
            return fib_iter(a - 1, y, x + y)

    return fib_iter(n, 0, 1)


known = {0: 0, 1: 1}


# @fn_timer
def fib4(n):
    if n in known:
        return known[n]
    res = fib4(n - 1) + fib4(n - 2)
    known[n] = res
    return res


if __name__ == '__main__':
    z = input("num=")
    # print fib3(z)
    print fib4(z)
