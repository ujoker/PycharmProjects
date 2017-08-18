# -*- coding: UTF-8 -*-

import datetime


if __name__ == '__main__':
    while True:
        now = datetime.datetime.now()
        print now.hour, now.minute
        if now.hour == 10 and 10 <= now.minute < 11:
            print 'hello world'
