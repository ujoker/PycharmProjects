#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
from r_w_txt import write_data_to_file


def gen_random(num):
    rand_list = range(0, num)
    for i in rand_list:
        rand_list[i] = random.randint(1, num)
    return rand_list

if __name__ == '__main__':
    write_data_to_file("a.txt", gen_random(100000))
