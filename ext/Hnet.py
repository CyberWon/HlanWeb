#!/usr/bin/python
#coding:utf-8
import pycurl
import StringIO

def hCurl(url):
    res={}
    b = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL,url)
    c.setopt(pycurl.CONNECTTIMEOUT,5)
    c.setopt(pycurl.TIMEOUT,5)
    c.setopt(pycurl.NOPROGRESS,1)
    c.setopt(pycurl.FORBID_REUSE,1)
    c.setopt(pycurl.MAXREDIRS,1)
    c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    try:
        c.perform()
        NAMELOOKUP_TIME=c.getinfo(c.NAMELOOKUP_TIME)
        CONNECT_TIME=c.getinfo(c.CONNECT_TIME)
        PRETRANSFER_TIME=c.getinfo(c.PRETRANSFER_TIME)
        STARTTRANSFER_TIME=c.getinfo(c.STARTTRANSFER_TIME)
        TOTAL_TIME=c.getinfo(c.TOTAL_TIME)
        HTTP_CODE=c.getinfo(c.HTTP_CODE)
        SIZE_DOWNLOAD=c.getinfo(c.SIZE_DOWNLOAD)
        HEADER_SIZE=c.getinfo(c.HEADER_SIZE)
        SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)
        res['HTTP_CODE']=HTTP_CODE
        '''
        print "HTTP状态码: %s" % (HTTP_CODE)
        print "DNS解析时间: %.2f ms" % (NAMELOOKUP_TIME*1000)
        print "建立链接时间: %.2f ms" % (CONNECT_TIME*1000)
        print "准备传输时间: %.2f ms" % (PRETRANSFER_TIME*100)
        print "传输开始时间: %.2f ms" % (STARTTRANSFER_TIME*1000)
        print "传输结束总时间: %.2f ms" % (TOTAL_TIME*1000)
        print "下载数据包大小: %d bytes/s" % (SIZE_DOWNLOAD)
        print "HTTP头部大小: %d bytes" % (HEADER_SIZE)
        print "平均下载速度: %d bytes/s" % (SPEED_DOWNLOAD)
        '''
        return res
    except Exception as e:
        res['error']=e
        c.close()
if __name__=='__main__':
    print hCurl('http://www.baidu.com')