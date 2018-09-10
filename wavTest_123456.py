# -*- coding: UTF-8 -*-

import wave
import matplotlib.pyplot as plt
import numpy as np
import os


def getData(filepath):
    filepath = "raw_test\\f0000.wav"  # 添加路径
    print('--------------------------')
    print("测试:" + filepath)
    f = wave.open(filepath, 'rb')
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    # 常用的音频参数：nchannels:声道数sampwidth:量化位数（byte）framerate:采样频率nframes:采样点数
    print("声道数:", nchannels)
    print("量化位数:", sampwidth)
    print("采样频率:", framerate)
    print("采样点数:", nframes)

    # 1 2 8000 11904
    strData = f.readframes(nframes)  # 读取音频，字符串格式
    print("读取音频，字符串格式len:", len(strData))
    waveData = np.fromstring(strData, dtype=np.short)  # 将字符串转化为int
    print("将字符串转化为int len:", len(waveData))
    print(waveData)
    print(max(abs(waveData)))
    time = np.arange(0, nframes) * (1.0 / framerate)  # 采样点数 采样频率
    return waveData,time


fileList=["raw_test\\f0000.wav",
          "raw_test\\f0001.wav",
          "raw_test\\f0002.wav",
          "raw_test\\f0003.wav"]

index=1
plt.figure()
for path in fileList:
    # print(path)
    result = getData(path)
    # print(result[1])
    waveData1 = result[0] * 128.0 / (max(abs(result[0])))  # wave幅值归一化
    plt.subplot(len(fileList),1,index)
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title(path)
    plt.grid('on')#标尺，on：有，off:无。

    plt.plot(result[1],waveData1)
    # plt.scatter(result[1],waveData1, c='r', marker='o')# 画散点图
    # plt.legend('x1') # 设置图标

    index +=1
plt.show()

# print('-----------111-----------')
# waveData1 = waveData*1.0/(max(abs(waveData))) #wave幅值归一化
# print(len(waveData1))
# print(waveData1)
# # print(type(waveData))
#
# print('-----------222-----------')
# waveData2 = waveData*128.0/(max(abs(waveData)))
# print(len(waveData2))
# print(waveData2)
#
#
# # print(len(array2))
# # # waveData2 = np.(array2) # fromstring(array2,dtype=np.int32)#将字符串转化为int
# # print(len(waveData2))
# # waveData2 = waveData2*1.0/(max(abs(waveData2)))#wave幅值归一化
# # print(len(waveData2))
#
# print('-----------333-----------')
# # plot the wave
# # 函数说明：arange([start,] stop[, step,], dtype=None)
# # 根据start与stop指定的范围以及step设定的步长，生成一个 ndarray
# time = np.arange(0,nframes)*(1.0 / framerate)#采样点数 采样频率
# time2 = np.arange(0,nframes)*(1.0 / framerate)
# # time = np.arange(0,(nframes-2)/2)*(1.0 / framerate)
# # print(time)
# plt.figure()
#
#
# plt.subplot(2,1,1)
# plt.plot(time,waveData1)
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Single channel wavedata ")
# plt.grid('on')#标尺，on：有，off:无。
#
# plt.subplot(2,1,2)
# plt.plot(time2,waveData2)
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Single channel wavedata to app")
# plt.grid('on')#标尺，on：有，off:无。
# plt.show()



