#!/usr/bin/python
#coding:utf-8
from ext.conf import readFirewall,writeFW
from ext import mod_sys
from mod.pp import ppUP
import sys
def fw_header():
    print('''#!/bin/bash
IPT=/sbin/iptables
$IPT -F
$IPT -X
$IPT -A INPUT -i lo -p all -j ACCEPT
$IPT -A OUTPUT -o lo -p all -j ACCEPT''')
def fIP(v,fx):
    fx='INPUT' if fx=='in' else 'OUPUT' 
    for i in xrange(len(v)):
        if '->' in v[i]:
            frl=v[i].split('->')
            frP=frl[1].split(':')
            frPort=frP[1].split()
            for Port in xrange(len(frPort)):
                print('$IPT -A %s -s %s -p %s --dport %s -j ACCEPT'%(fx,frl[0],frP[0],frPort[Port]))
            continue
        print("$IPT -A %s -s %s -j ACCEPT" % (fx,v[i]))
def fPORT(v,fx,pt):
    fx='INPUT' if fx=='in' else 'OUTPUT' 
    for i in xrange(len(v)):
        print("$IPT -A %s -p %s --dport %s -j ACCEPT" % (fx,pt,v[i]))
def buildFW():
    s=mod_sys.__redirection__()
    sys.stdout=s
    fw_header()
    fr=readFirewall('test')                 #fr firewall Rules 防火墙规则
    fin=fr['in']
    fIP(fin['ip'],'in')
    fPORT(fin['tcp'],'in','tcp')
    fIP(fin['ip'],'out')
    fPORT(fin['tcp'],'out','tcp')
    writeFW(s.buff)
def mod_main(argvs):
    buildFW()
#     ppUP(ip, v, p)/
#     IPtablesFile(rules_one())
    
if __name__=='__main__':
    mod_main('1')