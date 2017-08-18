# -*-coding:utf-8-*-
import time
from genrand import gen_random


def randomized_quick_sort(a, l, r):
    if l < r:
        x = a[r]
        i = l
        j = r - 1
        p = l
        q = r - 1
        while i < j:
            while a[i] < x:
                i += 1
            while a[j] > x:
                j -= 1
                if j == l:
                    break
            if i < j:
                a[i], a[j] = a[j], a[i]
                if a[i] == x:
                    a[p], a[i] = a[i], a[p]
                    p += 1
                    i += 1
                if a[j] == x:
                    a[q], a[j] = a[j], a[q]
                    q -= 1
                    j -= 1
        a[i], a[r] = a[r], a[i]
        j = i - 1
        i = i + 1
        for k in range(l+1, p):
            a[k], a[j] = a[j], a[k]
            j -= 1
        for k in range(q+1, r-2):
            a[i], a[k] = a[k], a[i]
            i += 1
        randomized_quick_sort(a, l, j)
        randomized_quick_sort(a, i, r)
    else:
        return


data1 = list(map(int, raw_input().split()))
# data2 = list(map(int, raw_input().split()))
n = data1[0]
# a = data2
a = gen_random(10)
print a
start = time.clock()
randomized_quick_sort(a, 0, n - 1)
end = time.clock()
print('Running time: %s Seconds' % (end - start))
for aa in a:
    print aa,
