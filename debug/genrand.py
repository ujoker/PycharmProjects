#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random


def gen_random(num):
    rand_list = range(0, num)
    for i in rand_list:
        rand_list[i] = random.randint(1, 100)
    return rand_list

if __name__ == '__main__':
    gen_random(100000)
