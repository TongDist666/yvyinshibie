# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:14:02 2019

@author: TongDist
"""

import subprocess
import time
import os

class ProcessSpeech:
    #初始化  命令字典
    def __init__(self):
        #主要命令      [名称，开始的路径，关闭的路径]
        self.init_cmd_diction={'浏览器':['chrome',r'C:\Users\TongDist\AppData\Local\Google\Chrome\Application\chrome.exe','chrome.exe'],
                      '记事本':['notepad',r'notepad',r'notepad.exe'],
                      '微信':['WeChat',r'D:\WeChat\WeChat.exe','WeChat.exe'],
                      '连接宽带':['cbe97f4bd3fce7890f374cd1838a98d5',r'C:\Users\TongDist\AppData\Local\cbe97f4bd3fce7890f374cd1838a98d5\cbe97f4bd3fce7890f374cd1838a98d5.exe'],
                      '计算器':['calc',r'calc','calc.exe']}
        #命令可选参数
        self.init_cmd_dst={'百度':r'www.baidu.com',
                      '哔哩哔哩':r'www.bilibili.com',
                      'github':r'https://github.com/github'}
        
    
    def process(self,cmd_str):
        #获取相应命令字典
        def get_process_cmd(input_string):
            cmd_temp=[]
            if '关闭' in input_string:
                cmd_temp.append(0)
            else:
                cmd_temp.append(1)
            for key in self.init_cmd_diction.keys():
                if key in input_string or key==input_string:
                    cmd_temp.append(self.init_cmd_diction[key])
                    return cmd_temp
                
            print(r'speech no return!!')
            return False
        #运行命令
        def run_cmdEndWithExe(str_t):
            subprocess.Popen(str_t[1])
        #关闭命令
        def kill_cmdEndWithExe(str_t):
            os.system(r'taskkill /F /IM '+str_t[2])
        
    
        str_temp=get_process_cmd(cmd_str)
        if str_temp[0]==0:
            try:
                kill_cmdEndWithExe(str_temp[1])
            except:
                print('closing wrong!!')
            else:
                print('closing success!!')
        elif str_temp[0]==1:
            try:
                run_cmdEndWithExe(str_temp[1])
            except:
                print('running wrong!!')
            else:
                print('runing success!!')
        

if __name__=='__main__':
    pass
