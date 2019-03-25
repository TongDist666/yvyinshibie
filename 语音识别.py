# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:27:25 2019

@author: dell
"""

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '15828193'
API_KEY = 'M5phgWEKFojiMtwL6emAGkCS'
SECRET_KEY = 'MOrYgH1jp3oGjs3tjSC5r2w7NHVEE8h4'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

print(client)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
#re=client.asr(get_file_content('北京科技馆.pcm'), 'pcm', 16000, {
#    'dev_pid': 1536,
#})

re=client.asr(get_file_content('01.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})
print(re)