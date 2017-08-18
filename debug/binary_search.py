# Uses python2


def binary_search(a, x):
    left = 0
    right = n - 1
    if left > right:
        return -1
    while left <= right:
        mid = (left + right) / 2
        if a[mid] == x:
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

data = map(int, raw_input().split())
n = data[0]
a = data[1: n + 1]
for x in data[n + 2:]:
    print binary_search(a, x),
