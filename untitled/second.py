#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
from fibonacci import fib4
from r_w_txt import read_data_from_file
from r_w_txt import write_data_to_file


def gen_fib_from_data(input_list):
    fib_list = []
    for i in input_list:
        fib_list.append(fib4(i))
    return fib_list

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError:
        print "输入命令行参数错误!"
        sys.exit()
    input_file = ""
    output_file = ""
    input_dataList = []
    for op, value in opts:
        if op in ("-i", "--input"):
            input_file = value
            input_dataList = read_data_from_file(input_file)
            print input_dataList
        elif op in ("-o", "--output"):
            output_file = value
            output_dataList = gen_fib_from_data(input_dataList)
            write_data_to_file(output_file, output_dataList)
            print output_dataList
        elif op in ("-h", "--help"):
            print 'help what'
            sys.exit()
    print("error args: {}".format(args))
