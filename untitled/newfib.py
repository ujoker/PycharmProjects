from TotalTime import fn_timer


@fn_timer
def fib(n):
    x, y = 0, 1

    while n:
        x, y, n = y, x + y, n - 1
    return x

if __name__ == '__main__':
    z = input("num=")
    print fib(z)
