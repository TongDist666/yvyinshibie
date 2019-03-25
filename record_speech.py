# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:32:34 2019

@author: TongDist
录音
"""

import wave
from pyaudio import PyAudio,paInt16

framerate=16000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=5

class Speech:
    def __init__(self,framerate=16000,NUM_SAMPLES=2000,channels=1,sampwidth=2):
        self.framerate=framerate
        self.NUM_SAMPLES=NUM_SAMPLES
        self.channels=channels
        self.sampwidth=sampwidth


    def my_record(self,fileName):
        def save_wave_file(filename,data):
            '''save the date to the wavfile'''
            wf=wave.open(filename,'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.sampwidth)
            wf.setframerate(self.framerate)
            wf.writeframes(b"".join(data))
            wf.close()
        pa=PyAudio()
        stream=pa.open(format = paInt16,channels=self.channels,
                       rate=self.framerate,input=True,
                       frames_per_buffer=self.NUM_SAMPLES)
        my_buf=[]
        count=0
        while count<TIME*8:#控制录音时间
            string_audio_data = stream.read(self.NUM_SAMPLES)
            my_buf.append(string_audio_data)
            count+=1
            print('.')
        save_wave_file(fileName,my_buf)
        stream.close()
    

if __name__ == '__main__':
    s=Speech()
    s.my_record('123.wav')
    print('Done!') 
    #play()