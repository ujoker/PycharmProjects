# -*- coding: UTF-8 -*-
import subprocess
from r_w_txt import read_data_from_file


aa = read_data_from_file("srrdata_seq.txt")
print aa[0]
bb = aa[0].replace('\r','')
name = '/home/leon/%s.sra' % bb
print name
url = 'ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/%s/%s/%s.sra' % (bb[0:6], bb, bb)
cmd = 'wget -O %s %s' % (name, url)
print cmd
# subprocess.call(cmd, shell=True)
