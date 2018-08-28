# -*- coding: UTF-8 -*-
import pylab as pl
import scipy.signal as signal

# pylab 模块是一款由python提供的可以绘制二维，三维数据的工具模块，其中包括了绘图软件包matplotlib,其可以生成matab绘图库的图像。
# SciPy 库建立在 Numpy 库之上，提供了大量科学算法，主要包括这些主题：
# 特殊函数 (scipy.special)
# 积分 (scipy.integrate)
# 最优化 (scipy.optimize)
# 插值 (scipy.interpolate)
# 傅立叶变换 (scipy.fftpack)
# 信号处理 (scipy.signal)
# 线性代数 (scipy.linalg)
# 稀疏特征值 (scipy.sparse)
# 统计 (scipy.stats)
# 多维图像处理 (scipy.ndimage)
# 文件 IO (scipy.io)

#功能画一条曲线
pl.figure(figsize=(6,2)) #创建一个6*2 点(point)的图
pl.plot(signal.hanning(500))
pl.show()
