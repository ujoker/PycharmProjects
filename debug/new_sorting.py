# -*-coding:utf-8-*-
# from genrand import gen_random


def partition3(a, l, r):
    i = l - 1
    for j in range(l, r):
        if a[j] <= a[r]:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i


def randomized_quick_sort(a, l, r):
    if l < r:
        p = partition3(a, l, r)
        randomized_quick_sort(a, l, p)
        randomized_quick_sort(a, p + 1, r)
    else:
        return


data1 = list(map(int, raw_input().split()))
data2 = list(map(int, raw_input().split()))
n = data1[0]
a = data2
# a = gen_random(100000)
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print x,
