import fibonacci


def seq(x):
    seq_list = []
    for i in x:
        seq_list.append(fibonacci.fib(i))
    return seq_list

if __name__ == '__main__':
    num = input("num=")
    if not isinstance(num, int):
        print 'The num you have input is not int type!'
    else:
        seq_index = range(1, num+1)
        fibonacciList = seq(seq_index)
        print fibonacciList
