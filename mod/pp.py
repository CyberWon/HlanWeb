#coding:utf-8
from threading import Thread
from ext.conf import readServer,readProject
from mod.shell import execCmd
from ext.mod_ns import upload_sftp
import os
def mod_help(): #模块帮助,
    print 'python hlan.py test -m tomcat -a list #Show Project\npython hlan.py  test -m tomcat -a projectNum'
def out(gen): #遍历生成器函数
    for i in gen:
        if i:
            print(i)
def ppUP(ip,v,p):
    localFile=p['local_file']
    remoteFile=os.path.join(p['path'],p['file'])
    rs=upload_sftp(hostname=ip,password=v[1],username=v[0],port=v[2],local_dir=localFile,remote_dir=remoteFile)
    rs.run()
def projectExec(ip,v,p):
    try:
        execCmd(ip, v, p,rs=False)
    except Exception,e:
        print '%s:%s' %(ip,e)
    finally:
        pass
def projectStart(ip,v,p): #选择项目后开始处理的函数 
#     print p['stop']
#     print p
    ppUP(ip, v, p)
#     projectExec(ip,v,[p['stop']])
#     projectExec(ip,v,[p['start']])
def mod_main(argvs): #mod_main() hlan定义模块必须.代表脚本将参数传递给模块的开始
    yield False #hlan定义mod_main()必须参数 . 因为hlan需要接受的返回结果为生成器.
    try:
        if argvs[5]=='list':   #当list 请求时 列出模块列表
            for index,mn in enumerate(readProject(1, pl=True)):
                print index,mn
        else:  #没发生错误时候就开始处理项目了
            s=readProject(argvs[5])
            if s:
                T_thread=[]
                rs=readServer(s['host'])
                for ip in rs:
                    v=rs[ip]
                    print v
                    t=Thread(target=projectStart,args=(ip,v,s))
                    T_thread.append(t)
                for i in range(len(T_thread)):
                    t.setDaemon(True)
                    T_thread[i].start()
            else:
                print 'Project not exsit!' 
    except Exception,e: #当输入格式不对引发错误显示出模块的正确使用方法
        print e
if __name__=='__main__': #编写模块时候调试用
    argvs=['hlan.py','test','-m','tomcat','-a','wechat']
    out(mod_main(argvs))