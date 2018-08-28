# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
from pydub import AudioSegment ###需要安装pydub、ffmpeg
import wave
import io

# 把mp3路径扔进去，就能输出一个now.wav文件
def trans_mp3_to_wav(mp3filepath,wavfilepath):
    song = AudioSegment.from_mp3(mp3filepath)
    song.export(wavfilepath, format="wav")

def file_extension(path):
  return os.path.splitext(path)[1]


def mp3_to_wav(mp3filepath,wavfilepath):
    #先从本地获取mp3的bytestring作为数据样本
    fp=open(mp3filepath,'rb')
    data=fp.read()
    fp.close()
    aud=io.BytesIO(data)
    sound=AudioSegment.from_file(aud,format='mp3')
    raw_data = sound._data
    #写入到文件，验证结果是否正确。
    l=len(raw_data)
    f=wave.open(wavfilepath,'wb')
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(16000)
    f.setnframes(l)
    f.writeframes(raw_data)
    f.close()

# filepath = "chinese\\" #添加路径
filepath = r"E:\\raw\\newRaw\\raw\\" #添加路径
filename= os.listdir(filepath) #得到文件夹下的所有文件名称
i=0
j=0
for file in filename:
    filename =file.split(".")[0] #以“.”为分割点获取文件名
    filesuffix = file_extension(file)
    # print(filename)
    if filesuffix == '.mp3':
        path = filepath+file
        j+=1
        wavfile = "D:\\python\\python_audio_test\\testfile\\"+ str(j) + "_mp3_wav_" +filename + ".wav"
        print(j,"mp3:"+ path," wav:",wavfile)
        #trans_mp3_to_wav(path,wavfile)
        #mp3_to_wav(path,wavfile)

        # try:
        #     #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据。
        #     f = wave.open(path,"rb")
        #     #读取格式信息
        #     #一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
        #     #样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
        #     params = f.getparams()
        #     nchannels, sampwidth, framerate, nframes = params[:4]
        #     #常用的音频参数：nchannels:声道数sampwidth:量化位数（byte）framerate:采样频率nframes:采样点数
        #     if framerate == 44100:
        #         i+=1
        #         # print('------------',i,'-------------')
        #         print(i,'路径:' + path)
        #         # print("声道数:",nchannels)
        #         # print("量化位数:",sampwidth)
        #         # print("采样频率:",framerate)
        #         # print("采样点数:",nframes)
        #         #读取波形数据
        #         #读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
        #         #str_data  = f.readframes(nframes)
        #         #print("声音数据:",len(str_data))
        #     f.close()
        # except Exception:
        #     j+=1
        #     wavfile = "testfile\\"+ filename + ".wav"
        #     print(j,"读取mp3:"+ path," ",wavfile)
        #     trans_mp3_to_wav(path,wavfile)


