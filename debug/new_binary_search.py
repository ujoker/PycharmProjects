# -*-coding:utf-8-*-


def binary_search(a, x):
    left = 0
    right = n - 1
    if left > right:
        return -1
    while left <= right:
        mid = (left + right) / 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            if mid == left:
                return -1
            else:
                right = mid - 1
        elif x > a[mid]:
            if mid == right:
                return -1
            else:
                left = mid + 1

data1 = map(int, raw_input().split())
data2 = map(int, raw_input().split())
n = data1[0]
a = data1[1:]
if not n == len(a):
    print 'Input Error!'
else:
    for x in data2[1:]:
        print binary_search(a, x),
