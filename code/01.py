#-------------------------------------------------
# @Project -> File   ：pythoncode1 -> 01
# @Time              : 2020/10/28 15:54
# @Author            : 若梦
# @FileName          : 01.py
# @Software          : PyCharm
#-------------------------------------------------
import urllib.request
import headersdatastool
import ipproxytool
import requests
import json
import os
import time

start = time.time()  # 程序开始时间

#url = requests.get('http://pvp.qq.com/web201605/js/herolist.json').content

#jsonFile = json.loads(url)  # 提取json
jsonFile1 = open('../files/herolist.json')
jsonFile = json.loads(jsonFile1)
print(jsonFile)

x = 0  # 用于记录下载的图片张数

# 目录不存在则创建
hero_dir = 'D:\PyCharmworkpace/pythoncode1/ruomeng/programe/sky/files\pictures\skin2\\'
if not os.path.exists(hero_dir):
    os.mkdir(hero_dir)

for m in range(len(jsonFile)):

    ename = jsonFile[m]['ename']  # 编号

    cname = jsonFile[m]['cname']  # 英雄名字

    skinName = jsonFile[m]['skin_name'].split('|')  # 切割皮肤的名字，用于计算每个英雄有多少个皮肤

    skinNumber = len(skinName)

    # 下载图片,构造图片网址

    for bigskin in range(1, skinNumber + 1):
        urlPicture = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(
            ename) + '-bigskin-' + str(bigskin) + '.jpg'

        picture = requests.get(urlPicture).content  # 获取图片的二进制信息

        with open(hero_dir + cname + "-" + skinName[bigskin - 1] + '.jpg', 'wb') as f:  # 保存图片
            f.write(picture)
            x = x + 1
            print("正在下载....第" + str(x) + "张")

end = time.time()  # 程序结束时间
time_second = end - start  # 执行时间
print("共下载" + str(x) + "张,共耗时" + str(time_second) + "秒")

