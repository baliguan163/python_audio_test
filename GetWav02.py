# -*- coding: utf-8 -*-
import struct
with open(r'E:\raw\myZh\ds_wav\tts.data','rb') as f:
    f.seek(0,2)
    n=f.tell() #tell()方法返回的文件内的文件读/写指针的当前位置
    print('n:',n)
    f.seek(0,0)
    buf=f.read(n)
    m=int(n/4)#4是根据你数据的类型和你之前定义的buf长度确定
    print(m,n)
    print(struct.unpack_from(str(m)+'I', buf, 0))
