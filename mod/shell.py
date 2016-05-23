#!/usr/bin/python
#coding:utf-8
from ext.conf import readServer,readModule
from ext.mod_ns import run_cmd
import threading
def mod_help():
    pass
def execCmd(ip,v,g,rs=True):
    global mod_json
    if rs:
        m=readModule(g)
    else:
        m=g
    rs=run_cmd(hostname=ip,password=v[1],username=v[0],port=v[2],echo_cmd=m)
    res=rs.run()
    mod_json[ip]=res
#     if rs:
#         for i in res['value']:
#             print('%s:\n%s' %(res['ip'],bytes.decode((res['value'][i]))))
#     else:
#     print(res)
#     print('ip:%s') % (res['ip'])
#     print('status:%s')%(res['status'])
#     if res['status']=='ok':
#         for y in res['value']:
#             print('command:%s\n%s')%(y,res['value'][y])

def mod_main(argvs):
    global mod_json
    mod_json={}
    server_list=readServer(argvs[1])
    g=argvs[5]
    T_thread=[]
    for (server,v) in server_list.items():
        t=threading.Thread(target=execCmd,args=(server,v, g))
        T_thread.append(t)
    for i in range(len(T_thread)):
        t.setDaemon(True)
        T_thread[i].start()
    for i in range(len(T_thread)):
        fina_flag=True
        if T_thread[i].is_alive():
            while fina_flag:
                if T_thread[i].is_alive():
                    continue
                else:
                    fina_flag=False
    return mod_json
if __name__=='__main__':
    li=['hlan.py', 'my','-m', 'shell', '-a', 'disk']
    out=mod_main(li)
    for i in out:
        if i:
            print(i)