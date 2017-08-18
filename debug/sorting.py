# Uses python2
import random


def partition3(a, l, r):
    x = a[l]
    j = l - 1
    h = r
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j = j + 1
            a[i], a[j] = a[j], a[i]
        elif a[i] > x:
            a[h], a[i] = a[i], a[h]
            h = h - 1
            i = i - 1
    return j, h


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    # k = random.randint(l + 1, r)
    # a[l], a[k] = a[k], a[l]
    p, q = partition3(a, l, r)
    randomized_quick_sort(a, l, p)
    randomized_quick_sort(a, q + 1, r)


data1 = list(map(int, raw_input().split()))
data2 = list(map(int, raw_input().split()))
n = data1[0]
a = data2
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print x,
