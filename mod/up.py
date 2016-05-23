#!/usr/bin/python
#coding:utf-8
from ext.conf import requireMod
import os
def mod_check(mod_name):
    try:
        __import__(mod_name)
        return True
    except:
        return False
def mod_install(mod_name):
    try:
        CMD='python -m pip install %s --upgrade' % mod_name
        os.system(CMD)
        print('install complete') 
    except:
        print('python -m pip no install or no set environment path')
def mod_main(argvs):
    li=requireMod()
    for i in li:
        if mod_check(i):
            print('check mod %s success' % i)
        else:
            print('Start install %s' % i)
            mod_install(li[i]['package'])
if __name__=='__main__':
    mod_main('111')