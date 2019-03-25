# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:40:49 2019

@author: TongDist
腾讯云语音
"""

import RASRsdk

# 用户需修改为自己官网的appid，secretid与sectretkey
secret_key = 'kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP'
secretid = 'AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8'
appid = '1258883290'

# 识别引擎 8k_0 or 16k_0
engine_model_type = '16k_0'
# 结果返回方式 0：同步返回 or 1：尾包返回
res_type = 0
# 识别结果文本编码方式 0:UTF-8,1:GB2312,2:GBK,3:BIG5
result_text_format = 0
#  语音编码方式 1:wav 4:sp 6:skill
voice_format = 1
# 音频文件路径
filepath = "北京科技馆.pcm"
# 语音切片长度 cutlength<200000
cutlength = 64000
# 调用语音识别函数获得识别结果
result=RASRsdk.sendVoice(secret_key, secretid, appid, engine_model_type,res_type, result_text_format, voice_format, filepath,cutlength)

print(result)

