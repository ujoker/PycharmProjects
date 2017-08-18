class Fibonacci(object):
    def fib(self, x):
        if isinstance(x, int):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x >= 2:
                return self.fib(x - 1) + self.fib(x - 2)
            else:
                return 'The num you have input is not positive!'
        else:
            return 'The num you have input is not int type!'


if __name__ == '__main__':
    y = Fibonacci()
    print y.fib(input("num="))
