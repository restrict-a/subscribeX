import requests
import json
import time
import re
import logging
import traceback
import os
import random
import datetime
import utils

def main(event, context):
    # 初始化日志文件
    utils.initLog('log.txt')
    utils.clearLog()
    
    saveData('https://classccai.oss-cn-beijing.aliyuncs.com/speed.png', 'speed.png')
    
    saveData('https://classccai.oss-cn-beijing.aliyuncs.com/link_url.txt', 'link_url.txt')
    
    saveData('https://classccai.oss-cn-beijing.aliyuncs.com/v2ray.txt', 'v2ray.txt')
    
    saveData('https://classccai.oss-cn-beijing.aliyuncs.com/clash.yml', 'clash.yml')

def saveData(url, name):
    resp = requests.get(url)
    dirs = './subscribe'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dirs + '/' + name, 'w', encoding='utf-8') as f:
        f.write(resp.text)
        print(name+'生成成功')

# 主函数入口
if __name__ == '__main__':
    main("", "")
