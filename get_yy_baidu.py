# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:15:05 2019

@author: TongDist
"""

from aip import AipSpeech
class mySpeech:
    def __init__(self,APP_ID,API_KEY,SECRET_KEY):
        self.APP_ID=APP_ID
        self.API_KEY=API_KEY
        self.SECRET_KEY=SECRET_KEY
        self.client=AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
    
    def get_speech(self,fileName,fileType,HZ,model=1536):
        def get_file_content(filePath_t):
            with open(filePath_t, 'rb') as fp:
                return fp.read()
        re=self.client.asr(get_file_content(fileName), 
                      fileType, HZ, 
                      {'dev_pid': model,})
        #1737 英文

        if re['err_no']==0:
            return re['result'][0]
        else:
            return False
        

if __name__=='__main__':
    test_speech=mySpeech('15828193','M5phgWEKFojiMtwL6emAGkCS','MOrYgH1jp3oGjs3tjSC5r2w7NHVEE8h4')
    result=test_speech.get_speech('01.wav','wav', 16000)
    print(result)
