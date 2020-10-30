#-------------------------------------------------
# @Project -> File   ：pythoncode1 -> iptool
# @Time              : 2020/10/30 15:55
# @Author            : 若梦
# @FileName          : iptool.py
# @Software          : PyCharm
#-------------------------------------------------


                                            #获取随机的IP代理


import json
import random



def get_ipdata():
    file = open("../files/ippool.json","r")
    content = file.read()
    file.close()
    ip_py_list = json.loads(content)
    #print(ip_py_list)
    return ip_py_list

def get_proxy():
    ip_value_datas = get_ipdata()#获得的ip列表
    #获取随机值
    index = random.randint(0,len(ip_value_datas)-1)
    return ip_value_datas[index]#获取的随机ip

if __name__ == '__main__':
    proxy = get_proxy()
    #print("获取的随机ip代理为：",proxy)