#!/usr/bin/python
# -*- coding: UTF-8 -*-


def read_data_from_file(filename):
    data_list = []
    datafile = open(filename)
    line = datafile.readline()
    while line:
        data = line.strip("\n")
        try:
            data_list.append(data)
        except ValueError, Argument:
            print "请检查文件内容！\n", Argument
        line = datafile.readline()
    datafile.close()
    return data_list


def write_data_to_file(filename, data_list):
    datafile = open(filename, "w")
    for i in range(len(data_list)):
        datafile.write(str(data_list[i]))
        datafile.write("\n")
    datafile.close()
