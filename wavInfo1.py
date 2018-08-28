# -*- coding: utf-8 -*-
import struct
import array

# wav是一种音频文件的格式，音频文件为二进制文件
# wav文件由头部信息和音频采样数据构成，前44个字节为头部信息
# 包括声道数 采样频率 PCM位宽等等，后面是音频采样数据

# 使用python 分析一个wav文件头部信息 处理音频数据
def main():
    with open(r'testFile\\m0000.wav','rb') as f:
        info=f.read(44)
        f.seek(0,2)
        print(f.tell())

        n=int((f.tell()-44)/2)
        buf=array.array('h',(0 for _ in range(n)))
        f.seek(44)
        f.readinto(buf)
        print(buf[0])
        print(buf[1])
        print(buf[2])

        for x in range(n):
            buf[x]= int(buf[x]/8)

        with open(r'testFile\\demo2.wav','wb') as f2:
            f2.write(info)
            buf.tofile(f2)

        info2=struct.unpack('h',b'\x01\x02')
        info3=struct.unpack('>h',b'\x01\x02')
        print(struct.unpack('h',info[22:24]))
        print(struct.unpack('i',info[24:28]))
        print(struct.unpack('h',info[34:36]))
        print(info2)
        print(info3)
    pass



main()

