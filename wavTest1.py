# -*- coding: UTF-8 -*-

import wave
import matplotlib.pyplot as plt
import numpy as np
import os

filepath = "E:\\raw\\raw\\test\\" #添加路径
filename= os.listdir(filepath) #得到文件夹下的所有文件名称
for file in filename:
    print('path:' + filepath+file)

print("get:"+filepath+filename[0])
f = wave.open(filepath+filename[0],'rb')
params = f.getparams()
print(params)

nchannels, sampwidth, framerate, nframes = params[:4]
#常用的音频参数：nchannels:声道数sampwidth:量化位数（byte）framerate:采样频率nframes:采样点数
print("nchannels:",nchannels," ",sampwidth," ",framerate," ",nframes)
#1 2 8000 11904
strData = f.readframes(nframes)#读取音频，字符串格式
strDataTT=strData
print(len(strData))

waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
print(len(waveData))

array2=[]
for i in range(0,len(waveData),2):
    array2.append(waveData[i])
    # print(i,' ',waveData[i])
print(len(array2))

print('-----------111-----------')
strDataT2=waveData
waveData = waveData*1.0/(max(abs(waveData))) #wave幅值归一化
print(len(waveData))
# print(type(waveData))
print('-----------222-----------')
waveData2 = strDataT2*128.0/32768 + 128
print(len(waveData2))
print('----------------------')

# print(len(array2))
# # waveData2 = np.(array2) # fromstring(array2,dtype=np.int32)#将字符串转化为int
# print(len(waveData2))
# waveData2 = waveData2*1.0/(max(abs(waveData2)))#wave幅值归一化
# print(len(waveData2))
print('----------------------')

# plot the wave
# 函数说明：arange([start,] stop[, step,], dtype=None)
# 根据start与stop指定的范围以及step设定的步长，生成一个 ndarray
time = np.arange(0,nframes)*(1.0 / framerate)
time2 = np.arange(0,nframes)*(1.0 / framerate)
# time = np.arange(0,(nframes-2)/2)*(1.0 / framerate)
print(time)
plt.figure()


plt.subplot(2,1,1)
plt.plot(time,waveData)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Single channel wavedata ")
plt.grid('on')#标尺，on：有，off:无。

plt.subplot(2,1,2)
plt.plot(time2,waveData2)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Single channel wavedata to app")
plt.grid('on')#标尺，on：有，off:无。
plt.show()



