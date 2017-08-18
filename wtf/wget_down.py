#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import datetime
import subprocess
import argparse


def read_data_from_file(filename):
    data_list = []
    inputfile = open(filename)
    line = inputfile.readline()
    while line:
        data = line.strip("\n")
        try:
            data_list.append(data)
        except ValueError, Argument:
            print "请检查文件内容！\n", Argument
        line = inputfile.readline()
    inputfile.close()
    return data_list


def download():
    srr_list = read_data_from_file(args.i)
    outputfile = open("none.txt", "a")
    for i in range(0, len(srr_list)):
        flag = 0
        while flag == 0:
            now = datetime.datetime.now()
            if not 7 < now.hour < 19:
                disk = os.statvfs("%ssra/" % args.o)
                if disk.f_bsize * disk.f_bavail > 7*1024*1024*1024:
                    srr = srr_list[i].replace('\r', '')
                    name = '%ssra/%s.sra' % (args.o, srr)
                    url = 'ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/%s/%s/%s.sra' % (srr[0:6], srr, srr)
                    cmd0 = 'wget -c -o %ssra/log/log%s.txt -P %ssra/ %s' % (args.o, srr, args.o, url)
                    cmd1 = 'tac %ssra/log/log%s.txt | sed -n 2p' % (args.o, srr)
                    cmd2 = 'rm -rf %ssra/%s.sra' % (args.o, srr)
                    if not os.path.exists(name):
                        try:
                            # print name
                            subprocess.call(cmd0, shell=True)
                            obj = subprocess.check_output(cmd1, shell=True)
                            if obj == '放弃操作。\n' or obj == 'Giving up.\n':
                                subprocess.call(cmd2, shell=True)
                        except KeyboardInterrupt:
                            outputfile.write(srr)
                            outputfile.write("\n")
                            outputfile.close()
                            sys.exit()
                        except:
                            outputfile.write(srr)
                            outputfile.write("\n")
                    flag = 1
                else:
                    print 'Out of Memory'
                    sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file")
    parser.add_argument("-o", help="output address")
    args = parser.parse_args()
    subprocess.call('mkdir %ssra/' % args.o, shell=True)
    subprocess.call('mkdir %ssra/log/' % args.o, shell=True)
    download()
