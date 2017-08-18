# -*- coding: UTF-8 -*-
import subprocess

# obj = subprocess.call('tac /home/sra/log/logSRR2113368.txt | sed -n 2p', shell=True)
obj = subprocess.check_output('tac /home/sra/log/logSRR2113368.txt | sed -n 2p', shell=True)
print obj
if obj == '放弃操作。\n' or obj == 'Giving up.\n':
    subprocess.call('rm -rf /home/sra/SRR2113368.sra', shell=True)
    print 'aaa'
else:
    print 'bbb'
