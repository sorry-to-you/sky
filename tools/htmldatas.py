#-------------------------------------------------
# @Project -> File   ：pythoncode1 -> htmldatas
# @Time              : 2020/10/30 9:27
# @Author            : 若梦
# @FileName          : htmldatas.py
# @Software          : PyCharm
#-------------------------------------------------

                                            #保存页面的ip




import urllib.request
import headersdatastool
import time
import lxml.html
import os
import json
def get_ip_url_list():
    url_list = []
    for index in range(1,6):
        http_url = "http://www.89ip.cn/index_"+str(index)+".html"
        #print(http_url)
        url_list.append(http_url)
    return url_list
def catch_ip_list(html_content):
    """分析数据"""
    ip_list = []
    #获取dtree对象
    metree = lxml.html.etree
    ip_parse = metree.HTML(html_content)
    tr_list = ip_parse.xpath("//table[@class='layui-table']/tbody/tr")
    # print(tr_list)
    # print(len(tr_list))
    for tr_element in tr_list:
        item = {}
        #IP值
        temp_ip = tr_element.xpath("./td[1]/text()")
        ip = temp_ip[0].strip()
        #print(ip)
        #端口号
        temp_port = tr_element.xpath("./td[2]/text()")[0]
        port = temp_port.strip()
        #print(port)
        value = "https://"+ip+":"+port
        #print(value)
        item["https:"] = value
        #print(item)
        ip_list.append(item)
        #print("页面的IP代理数据",ip_list)
    return ip_list

    #获取解析对象
    #开始解析

def save_ip_file(datas):
    """保存所爬取的数据的IP"""
    path = "../files"
    if not os.path.exists(path):
        os.mkdir(path)
    #保存数据
    json_strs = json.dumps(datas,indent=2)
    #print(type(json_strs))
    file = open(path+"/ipdatas.json","w")
    file.write(json_strs)
    file.close()
    print("所有代理数据保存成功！")


def pares_http_url(temp_url):
    """爬取网页源代码"""
    #设定headers
    request = urllib.request.Request(temp_url,headers=headersdatastool.get_headers())
    ip_response = urllib.request.urlopen(request)
    html_content = ip_response.read().decode('utf-8')
    return html_content
def main():
    #批量查询五页
    ip_url_datas = get_ip_url_list()
    #print(ip_url_datas)
    #列表
    all_ip_datas = []
    for http_url in ip_url_datas:
        ip_html_datas = pares_http_url(http_url)
        #分析源代码
        html_ip_list = catch_ip_list(ip_html_datas)
        #print(ip_html_datas)以什么方式保存数据大就列表
        all_ip_datas.extend(html_ip_list)
        time.sleep(3)
    #print("所有的IP代理数据",all_ip_datas)
    save_ip_file(all_ip_datas)
if __name__ == '__main__':
    main()