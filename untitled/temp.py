
def fib1(n):
    if n == 0 or n == 1:
        return n
    if n >= 2:
        return fib1(n-1) + fib1(n-2)
    else:
        return


if __name__ == '__main__':
    z = input("num=")
    print fib1(z)
