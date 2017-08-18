# -*- coding: UTF-8 -*-
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="input file")
parser.add_argument("-o", help="output address")
args = parser.parse_args()
print args.i, args.o
obj = subprocess.call('mkdir %s/test/' % args.o, shell=True)
