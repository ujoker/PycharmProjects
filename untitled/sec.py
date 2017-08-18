#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
# from fibonacci import fib5
import fibonacci
from r_w_txt import read_data_from_file
from r_w_txt import write_data_to_file
from TotalTime import fn_timer


def gen_fib_from_data(input_list):
    fib_list = []
    for i in input_list:
        # if i > len(fibonacci.known):
            # for zz in range(len(fibonacci.known), i):
                # fibonacci.fib4(zz)
        fib_list.append(fibonacci.fib6(i))
    return fib_list


@fn_timer
def data_fib():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", choices=['aa.txt', 'bb.txt'], help="input file")
    parser.add_argument("-o", choices=['aa.txt', 'bb.txt'], help="output file")
    args = parser.parse_args()
    aa_list = read_data_from_file(args.i)
    # print aa_list
    bb_list = gen_fib_from_data(aa_list)
    write_data_to_file(args.o, bb_list)
    # print bb_list

if __name__ == '__main__':
    data_fib()
