# shell模块文档

## 被调用

```python
from mod.shell import execCmd	#导入模块
execCmd(ip, v, p,rs=False)		#执行并且传递给参数
```

|   参数  | 代表值       | 解释                                              |
| :--------:  | :-----:      | :----:                                            |
|     ip     | 192.168.1.1      | str类型。代表    ip地址                                     |
|   v       |['root','6666',22] | list或者tuple类型。代表链接账号信息                    |
|   p       |["cmd1","cmd2"] | list或者tuple类型。代表要执行的命令                   |
|   rs		| Ture Or False | bool型，False代表p的参数为list，True代表着去调用readModule来转换成list|	
