import sys
import getopt


def read_data_from_file(filename):
    data_list = []
    datafile = open(filename)
    line = datafile.readline()
    while line:
        data = line.strip("\n")
        data_list.append(data)
        line = datafile.readline()
    datafile.close()
    return data_list

opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
input_file = ""
output_file = ""

for op, value in opts:
    if op == "-i":
        input_file = value
        print input_file
        input_dataList = read_data_from_file(input_file)
        print input_dataList
    elif op == "-o":
        output_file = value
    elif op == "-h":
        print 'help'
        sys.exit()
