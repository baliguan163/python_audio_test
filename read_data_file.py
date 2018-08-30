#coding=utf-8
import os
import struct
import wave
import numpy as np


# 清空目录
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

def save_wave_file(filename,buf):
    # wav文件写入
    waveData = np.fromstring(buf, dtype=np.int16)  # 将字符串转化为int

    print(waveData)
    # waveData = waveData * 1.0 / (max(abs(waveData)))  # wave幅值归一化print(waveData)
    # print(waveData)
    nchannels = 1
    sampwidth = 2
    fs = 16000
    data_size = len(waveData)
    framerate = int(fs)
    nframes = data_size
    print(data_size)
    print(framerate)
    print(nframes)

    # print(framerate, nframes,)
    comptype = "NONE"
    compname = "not compressed"
    outwave = wave.open(filename, 'wb')  # 定义存储路径以及文件名
    outwave.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    for v in waveData:
        # temp=v * 64000 / 2
        # temp = ((v  *128.0) / 32768.0) + 128.0
        # print(v)
        outwave.writeframes(struct.pack('h',int(v)))  # outData:16位，-32767~32767，注意不要溢出
    outwave.close()

# struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流
# ，或字节数组）。其函数原型为：struct.pack(fmt, v1, v2, …)，参数fmt是格式字符串，关于格式字符串的相关信息在下面有
# 所介绍。v1, v2, …表示要转换的python值
# 640032
# 640144   110
# 640288   144
# 640368   120
# f=open(r"D:\raw\mydata\tts.data",'rb')
del_file('D:\\raw\\mydata\\tts\\')

f=open(r"ttsdata\tts_en.data",'rb')
f.seek(640032,0)
i=0
while f:
    buf=f.read(7100)
    if len(buf) == 0:
        print('-------------------------')
        break;
    # name = r'D:\raw\mydata\tts\%s.wav' % i
    name = r'D:\raw\mydata\tts\%s.wav' % i
    i += 1
    print("---------------------------------------------------------------")
    print(i,name,len(buf))
    save_wave_file(name,buf)
f.close()
