# -*- coding: utf-8 -*-

#语谱图:其实得到了分帧信号，频域变换取幅值，就可以得到语谱图，
## 如果仅仅是观察，matplotlib.pyplot有specgram指令：
import wave
import matplotlib.pyplot as plt
import numpy as np
import os

filepath = "raw_test\\" #添加路径
filename= os.listdir(filepath) #得到文件夹下的所有文件名称

print(filepath+filename[1])
f = wave.open(filepath+filename[1],'rb')


params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
#常用的音频参数：nchannels:声道数sampwidth:量化位数（byte）framerate:采样频率nframes:采样点数
print("声道数:",nchannels)
print("量化位数:",sampwidth)
print("采样频率:",framerate)
print("采样点数:",nframes)

strData = f.readframes(nframes)#读取音频，字符串格式
# print(strData)
waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
print(waveData)
waveData = waveData*128.0/(max(abs(waveData)))#wave幅值归一化
print(waveData)

waveData = np.reshape(waveData,[nframes,nchannels]).T
f.close()
print(waveData)

time = np.arange(0, nframes) * (1.0 / framerate)  # 采样点数 采样频率

# plot the wave  采样频率
plt.specgram(waveData[0],Fs = framerate, scale_by_freq = True, sides = 'default')
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')

plt.show()
