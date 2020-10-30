#-------------------------------------------------
# @Project -> File   ：pythoncode1 -> ipvaluedataspider
# @Time              : 2020/10/30 15:11
# @Author            : 若梦
# @FileName          : ipvaluedataspider.py
# @Software          : PyCharm
#-------------------------------------------------

                                            ##制作代理池



import json
import os
import requests
import headersdatas
def read_ipdata_file_from_json():
    """从IP。data。json读取"""
    file = open("../files/ipdatas.json","r")
    ipcotent = file.read()
    file.close()
    # print(ipcotent)
    # print(type(ipcotent))
    py_ip_list = json.loads(ipcotent)
    #print(type(py_ip_list))
    return py_ip_list



def main():
     #制作代理池
#（1）读取IP数据文件
    ip_datas = read_ipdata_file_from_json()
    ip_value_list = []
    for element in ip_datas:
        # print(element)推荐不要使用百度。com验证ip可用性
        #https://www.sohu.com
        html_url = "https://www.sohu.com"
        response = requests.get(html_url,
                                headers=headersdatas.get_headers(),
                                proxies=element)
         #200请求成功
        if response.status_code==200:
            print("ip代理有效",element)
            ip_value_list.append(element)
            json_strs = json.dumps(ip_value_list,indent=2)
            with open("../files/ippool.json","w")as file:
                file.write(json_strs)
                print("ip代理池新增的一个ip。。。。")

             #存到代理池







if __name__ == '__main__':
    main()