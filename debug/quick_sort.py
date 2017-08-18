# -*-coding:utf-8-*-
import time
from genrand import gen_random
import sys


sys.setrecursionlimit(100000000)


def quick_sort(lists, left, right):
    low = left
    high = right
    if low >= high:
        return lists
    key = lists[low]
    while low < high:
        while low < high and lists[high] > key:
            high -= 1
        lists[low] = lists[high]
        while low < high and lists[low] <= key:
            low += 1
        lists[high] = lists[low]
    lists[high] = key
    quick_sort(lists, left, low - 1)
    quick_sort(lists, low + 1, right)
    return lists


data1 = list(map(int, raw_input().split()))
# data2 = list(map(int, raw_input().split()))
n = data1[0]
# a = data2
a = gen_random(100000)
start = time.time()
aa = quick_sort(a, 0, n - 1)
end = time.time()
print('Running time: %f Seconds' % (end - start))
for x in aa:
    print x,
