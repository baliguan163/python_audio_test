import shutil
import wave
# import matplotlib.pyplot as plt
# import numpy as np
import os

global fail
global ok
fail=0
ok=0

def deleteNullFile(src):
    '''删除所有大小为0的文件'''
    files = os.listdir(src)
    k=0
    for file in files:
        print('path:' + src + file)
        if os.path.getsize(file) == 0:   #获取文件大小
            print(file)
            os.remove(file)
            k+=1
            print(k," deleted." + file)

# 从2channel，4.41k hz 重采样到 1 channel，16k hz
def downsampleWav2_1(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
    global ok
    global fail
    import os,wave,audioop
    if not os.path.exists(src):
        print ('Source not found!')
        return False
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    try:
        s_read = wave.open(src, 'r')
    except:
        print ('Failed to open files!')
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)

# audioop.ratecv(fragment, width, nchannels, inrate, outrate, state[, weightA[, weightB]])
# 转换输入片段的帧频。
# state是包含转换器状态的元组。转换器返回一个元组(newfragment, newstate)，并且newstate应该被传递给下一个
# 调用ratecv()。最初的呼叫应该None作为状态传递。
# 的weightA和weightB参数是一个简单的数字滤波器和默认参数以1及0分别。
    try:
        converted = audioop.ratecv(data,2,inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)

# audioop.tomono(fragment, width, lfactor, rfactor)
# 将立体声片段转换为单声道片段。左声道乘以lfactor，右声道乘以rfactor，然后再添加两个声道以提供单声道信号。
    except:
        fail += 1
        print(fail,'Failed to downsample wav',src, dst)
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False
    try:
        s_write = wave.open(dst, 'w')
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        s_write.close()
        print ('Failed to write wav')
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False
    try:
        s_read.close()
        s_write.close()
    except:
        print ('Failed to close wav files')
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False

    ok+=1
    print(ok,'转换成功:',src, dst)
    return True

# 若in和out都是单通道：
def downsampleWav1_1(src, dst, inrate=44100, outrate=16000, inchannels=1, outchannels=1):
    global ok
    global fail
    import os, wave, audioop
    if not os.path.exists(src):
        print('Source not found!')
        return False
    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))
    try:
        s_read = wave.open(src, 'rb')
        params = s_read.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        # print(nchannels, sampwidth, framerate, nframes)
    except:
        print('Failed to open files!')
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)
    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1 and inchannels != 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print('Failed to downsample wav')
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False
    try:
        s_write = wave.open(dst, 'wb')
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted[0])
    except Exception as e:
        print(e)
        print('Failed to write wav')
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print('Failed to close wav files')
        shutil.copyfile(src, outpath1600_exception)  # 拷贝文件
        return False

    ok+=1
    print(ok,'转换成功:',src, dst)
    shutil.copyfile(path, outpath16000)  # 拷贝文件
    return True



def file_extension(path):
  return os.path.splitext(path)[1]

# 清空目录
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


# filepath = "chinese\\" #添加路径
filepath = "E:\\raw\\44100_to_16000\\44100_exception_to_temp\\" #添加路径
filename= os.listdir(filepath) #得到文件夹下的所有文件名称
i=0
j=0
del_file("E:\\raw\\44100_to_16000\\44100_exception_to_temp_16000\\")

for file in filename:
    path = filepath+file
    filename =file.split(".")[0] #以“.”为分割点获取文件名
    outpath16000 = "E:\\raw\\44100_to_16000\\44100_exception_to_temp_16000\\" + filename + ".wav"
    try:
        #打开wav文件 ，open返回一个的是一个Wave_read类的实例，通过调用它的方法读取WAV文件的格式和数据。
        f = wave.open(path,"rb")
        #读取格式信息
        #一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：声道数, 量化位数（byte单位）, 采
        #样频率, 采样点数, 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
        params = f.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]
        #常用的音频参数：nchannels:声道数sampwidth:量化位数（byte）framerate:采样频率nframes:采样点数
        if framerate == 44100:
            i+=1
            # print('------------',i,'-------------')
            # print(i, '文件路径:' + path, outpath44100, outpath16000)
            # print("声道数:",nchannels)
            # print("量化位数:",sampwidth)
            # print("输出文件:",outpath16000)
            # print("采样频率:",framerate)
            # print("采样点数:",nframes)
            #读取波形数据
            #读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位）
            #str_data  = f.readframes(nframes)
            #print("声音数据:",len(str_data))
            downsampleWav2_1(path, outpath16000)
            # downsampleWav1_1(path, outpath16000)
        f.close()
    except Exception:
        j+=1
        # shutil.copyfile(path, outpath1600_exception)  # 拷贝文件
        print(j,'异常文件:' + path,outpath16000)

print('-------------------------------------------------')
# delete16000 = "E:\\raw\\44100_to_16000\\16000\\"
# deleteNullFile(delete16000);
