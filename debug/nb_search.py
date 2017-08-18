# -*- coding: UTF-8 -*-


def nb_search(data_list, find_list, key, flag=0):
    left = 0
    right = len(data_list) - 1
    while left <= right:
        mid = (left + right) / 2
        if find_list[0:key] == data_list[mid][0:key]:
            return mid
        elif find_list[0:key] < data_list[mid][0:key]:
            right = mid - 1
        else:
            left = mid + 1
    if flag == 1:
        return left
    return -1


def nb_insert(data_list, insert_list, key):
    pos = nb_search(data_list, insert_list, key, 1)
    data_list.insert(pos, insert_list)


data1 = []
print data1
data2 = [u'1', u'4', u'G', u'6', u'9', u'2']
data3 = [u'2', u'3', u'A', u'6', u'2', u'5']
data4 = [u'1', u'4', u'C', u'9', u'2', u'3']
# nb_insert(data1, data2, 3)
print data1
# nb_insert(data1, data3, 3)
print data1
# nb_insert(data1, data4, 3)
print data1
print nb_search(data1, data3, 3)
