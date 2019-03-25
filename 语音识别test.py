# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:47:41 2019

@author: TongDist
"""

import get_yy_baidu as getyy
import record_speech as record

s_temp=record.Speech(framerate=16000,NUM_SAMPLES=2000,channels=1,sampwidth=2)
s_temp.my_record('test.wav')
g_temp=getyy.mySpeech('15828193','M5phgWEKFojiMtwL6emAGkCS','MOrYgH1jp3oGjs3tjSC5r2w7NHVEE8h4')

#result=g_temp.get_speech('test.wav','wav', 16000,1737)
result=g_temp.get_speech('test.wav','wav', 16000)
print(result)