# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: dg
import time, os, sys, random
from time import sleep as timeout

def subscribe():
    print '\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1m Loading..'
    time.sleep(1)
    print '\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1m Sedang Membuka Youtube'
    time.sleep(1)
    os.system('xdg-open https://www.youtube.com/channel/UClb7JaAMtvIrBtRsFEbFZmg')
    time.sleep(1)
    os.system('clear')
    os.system('sh __client__.sh')


if __name__ == '__main__':
    subscribe()