# -*-coding:utf-8-*-
from genrand import gen_random
import time


a = gen_random(100000)
start = time.time()
a.sort()
end = time.time()
print('Running time: %s Seconds' % (end - start))
for aa in a:
    print aa,
