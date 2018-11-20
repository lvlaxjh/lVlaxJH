# -*- coding: utf-8 -*-
import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display

def Soundprocessing(_mpath):
    _y,_sr=librosa.load(_mpath,sr=None)
    print(type(_y),_y)
    print(type(_sr),_sr)
    _melspec=librosa.feature.melspectrogram(_y,_sr,n_fft=1024, hop_length=512, n_mels=128)
    _logmelspec=librosa.power_to_db(_melspec)
    print(type(_logmelspec.shape),_logmelspec.shape)
    _mfccs=librosa.feature.mfcc(y=_y,sr=_sr,n_mfcc=40)
    print(type(_mfccs.shape),_mfccs.shape)
    plt.figure()
    plt.subplot(2,1,1)
    librosa.display.waveplot(_y,_sr)
    plt.title('Beat wavform')
    plt.subplot(2,1,2)
    librosa.display.specshow(_logmelspec,sr=_sr,x_axis='time',y_axis='mel')
    plt.title('Mel wavform')
    plt.tight_layout()
    plt.show()

_mpath='test3.wav'
Soundprocessing(_mpath)
_mpath='test2.wav'
Soundprocessing(_mpath)
_mpath='test.wav'
Soundprocessing(_mpath)