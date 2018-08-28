# -*- coding: utf-8 -*-

#语谱图:其实得到了分帧信号，频域变换取幅值，就可以得到语谱图，
## 如果仅仅是观察，matplotlib.pyplot有specgram指令：
import wave
import matplotlib.pyplot as plt
import numpy as np
import os

filepath = "E:\\raw\\raw\\test\\" #添加路径
filename= os.listdir(filepath) #得到文件夹下的所有文件名称
f = wave.open(filepath+filename[1],'rb')

params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)#读取音频，字符串格式
waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化

waveData = np.reshape(waveData,[nframes,nchannels]).T
f.close()
# plot the wave
plt.specgram(waveData[0],Fs = framerate, scale_by_freq = True, sides = 'default')
plt.ylabel('Frequency(Hz)')
plt.xlabel('Time(s)')
plt.show()
