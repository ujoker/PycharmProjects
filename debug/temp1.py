# -*-coding:utf-8-*-
# from genrand import gen_random


def randomized_quick_sort(a, l, r):
    if l < r:
        x = a[r]
        i = l
        j = r - 1
        p = l
        q = r - 1
        print x, i, j, p, q
        while i < j:
            while a[i] < x:
                i += 1
                print i, 'i'
            while a[j] > x:
                j -= 1
                print j, 'j'
                if j == l:
                    break
            print i, j
            if i < j:
                a[i], a[j] = a[j], a[i]
                print a
                if a[i] == x:
                    a[p], a[i] = a[i], a[p]
                    p += 1
                    # i += 1
                    print a, 'a'
                if a[j] == x:
                    a[q], a[j] = a[j], a[q]
                    q -= 1
                    # j -= 1
                    print a, 'aa'
                i += 1
                j -= 1
                print i, j
        print i, r
        a[i], a[r] = a[r], a[i]
        print a, 'aaa'
        j = i - 1
        i = i + 1
        print l, p, 'l', 'p'
        for k in range(l+1, p):
            a[k], a[j] = a[j], a[k]
            j -= 1
        print a, 'aaaa'
        print q, r, 'q', 'r'
        for k in range(q+1, r):
            a[i], a[k] = a[k], a[i]
            i += 1
        print a, 'aaaaa'
        randomized_quick_sort(a, l, j)
        randomized_quick_sort(a, i, r)
    else:
        return


data1 = list(map(int, raw_input().split()))
data2 = list(map(int, raw_input().split()))
n = data1[0]
a = data2
# a = gen_random(100000)
randomized_quick_sort(a, 0, n - 1)
for aa in a:
    print aa,
