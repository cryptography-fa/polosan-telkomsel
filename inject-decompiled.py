# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: dg
import time, os, sys, random
from time import sleep as timeout

def rus(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)


def tes(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)


sys.stdout.write('\x1b]2;POLOSAN TELKOMSEL @Mr.Tr3v!0n Channel Youtube: Tutorial Android\x07')
os.system('clear')
print '\x1b[32;1m    __________________________'
time.sleep(1)
rus('\n\x1b[39;1m     Jangan lupa subscribe \n     channel youtube admin\n     dan aktifkan notifikasi \n     lonceng nya...\n')
print '\x1b[32;1m    __________________________'
print '\n'

def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


def subscribe():
    print '\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1m Loading..'
    time.sleep(1)
    print '\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[32;1m Sedang Membuka Youtube'
    time.sleep(1)
    os.system('xdg-open https://www.youtube.com/channel/UClb7JaAMtvIrBtRsFEbFZmg')
    time.sleep(1)
    os.system('clear')
    pilih()


def menu():
    os.system('sh __client__.sh')


def pilih():
    print '\x1b[39;1m[\x1b[32;1m01\x1b[39;1m]\x1b[32;1m Subsribe Gratis'
    print '\x1b[39;1m[\x1b[32;1m02\x1b[39;1m]\x1b[32;1m Polosan Telkomsel'
    print '\x1b[39;1m[\x1b[32;1m00\x1b[39;1m]\x1b[31;1m Keluar\n'
    x = raw_input('\x1b[39;1m[\x1b[32;1m+\x1b[39;1m]\x1b[34;1mPILIH NOMOR\x1b[31;1m: \x1b[39;1m')
    if x == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih()
    else:
        if x == '01':
            subscribe()
        else:
            if x == '02':
                menu()
            else:
                if x == '00':
                    keluar()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + x + ' \x1b[1;91mTidak ada'
                    pilih()


if __name__ == '__main__':
    pilih()