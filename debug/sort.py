# -*-coding:utf-8-*-


def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        j = i - 1
        key = lists[i]
        while j >= 0:
            if lists[j] > key:
                lists[j+1], lists[j] = lists[j], key
            j -= 1
    return lists


def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(group):
            j = i + group
            while j < count:
                key = lists[j]
                k = j - group
                while k >= 0:
                    if lists[k] > key:
                        lists[k+group], lists[k] = lists[k], key
                    k = k-group
                    print k, lists
                j += group
        print 'a'
        group = group/step
        print group
    return lists


if __name__ == '__main__':
    data = list(map(int, raw_input().split()))
    ll = data
    print shell_sort(ll)
