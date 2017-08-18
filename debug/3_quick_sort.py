# -*-coding:utf-8-*-
import time
from genrand import gen_random


def randomized_quick_sort(a, l, r):
    if r <= l:
        return
    x = a[r]
    i = l
    j = r - 1
    p = l
    q = r - 1
    while True:
        while i < r and a[i] <= x:
            if a[i] == x:
                a[p], a[i] = a[i], a[p]
                p += 1
            i += 1
        while j >= l and a[j] >= x:
            if a[j] == x:
                a[q], a[j] = a[j], a[q]
                q -= 1
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    i -= 1
    p -= 1
    while p >= l:
        a[i], a[p] = a[p], a[i]
        i -= 1
        p -= 1
    j += 1
    q += 1
    while q <= r:
        a[j], a[q] = a[q], a[j]
        j += 1
        q += 1

    randomized_quick_sort(a, l, i)
    randomized_quick_sort(a, j, r)


data1 = list(map(int, raw_input().split()))
data2 = list(map(int, raw_input().split()))
n = data1[0]
c = data2
# c = gen_random(100000)
start = time.time()
randomized_quick_sort(c, 0, n - 1)
end = time.time()
print('Running time: %s Seconds' % (end - start))
for aa in c:
    print aa,
