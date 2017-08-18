# -*- coding: UTF-8 -*-
import subprocess


url = "ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR210/SRR2107510/SRR2107510.sra"
# name = '/home/leon/SRR2119179.sra'
cmd = 'wget -S --spider %s' % url

subprocess.call(cmd, shell=True)
