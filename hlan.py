#!/usr/bin/python
#coding:utf-8
import sys,json
from ext.hlan import extHlanMain
#帮助信息,
def main_help(): 
    return '''python hlan.py host-group/host-ip/host-name -m mod_name  -a 'mod_args'
    eg:python hlan.py 127.0.0.1 -m shell -a 'free -m'
'''
#模块路径
@extHlanMain(sp='.')                            #以什么做分割
def main(argvs):
    try:
        #使用反射机制加载模块
        load_mod=__import__(argvs[3]) 
        #将环境参数传递给模块去处理.模块返回的是生成器,需要遍历才能输出
        if argvs[5]=='help':
            mod_out=load_mod.mod_help()
        else:    
            mod_out=load_mod.mod_main(argvs) 
        return json.dumps(mod_out)
    #载入不存在模块时候或者 模块不存在mod_main()时候 提示.
    except Exception as e: 
#     except:
        return e
if __name__=='__main__':
    #将脚本后面的环境变量交给main函数去执行
    print main(sys.argv)
