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
import urllib.request

def main(event, context):
    # 初始化日志文件
    utils.initLog('log.txt')
    utils.clearLog()
    
    dirs = './subscribe'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    
    saveImage('https://classccai.oss-cn-beijing.aliyuncs.com/speed.png', dirs + '/' + 'speed.png')

    saveData('https://classccai.oss-cn-beijing.aliyuncs.com/link_url.txt', dirs + '/' + 'link_url.txt')
    
    saveData('https://classccai.oss-cn-beijing.aliyuncs.com/v2ray.txt', dirs + '/' + 'v2ray.txt')
    
    saveData('https://classccai.oss-cn-beijing.aliyuncs.com/clash.yml', dirs + '/' + 'clash.yml')
    
    
def saveImage(url, path):
    urllib.request.urlretrieve(url, path)
    print(path + '生成成功')
        
def saveData(url, path):
    resp = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(resp.content, encoding = "utf8"))
        print(path + '生成成功')

# 主函数入口
if __name__ == '__main__':
    main("", "")
