#coding:utf-8
'''
对hlan的扩展
'''
def extHlanMain(sp=''):
    def _extHlanMain(func):
        def __extHlanMain(argvs):
            li=argvs[1].split(sp)
            li.insert(0,'hlan.py')
            li.insert(2,'-m')
            li.insert(4,'-a')
            return func(li)
        return __extHlanMain
    return _extHlanMain