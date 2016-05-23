#!/usr/bin/python
#coding:utf-8
import hlan,sys
from ext import mod_sys
from ext.conf import writeWxHTML
import json

def hlan_main(wx_content):
    s=mod_sys.__redirection__()
    sys.stdout=s
    li=['hlan.py',wx_content]
    try:
        hlan.main(li)
        res=json.loads(s.buff.replace('\'', '"'))
        s.reset()
        WxRes="<pre>\n"
        for k in res:
            if k=='active':
                pass
            else:
                WxRes+='%s:\n'%k
                res_value=res[k]['value']
                for i in res_value:
                    WxRes+='%s\n'% res_value[i]
        WxRes+='</pre>'
        writeWxHTML(WxRes, wx_content)
        return '生成成功了。'
    except Exception as e:
        return '生成失败了'
if __name__=='__main__':
    print hlan_main('my.shell.11')