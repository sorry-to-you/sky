#-------------------------------------------------
# @Project -> File   ：pythoncode1 -> htmldatas
# @Time              : 2020/10/30 9:27
# @Author            : 若梦
# @FileName          : htmldatas.py
# @Software          : PyCharm
#-------------------------------------------------
import urllib.request
import headersdatas
import time


def get_ip_url_list():
    url_list = []
    for index in range(1,6):
        http_url = "http://www.89ip.cn/index_"+str(index)+".html"
        #print(http_url)
        url_list.append(http_url)
    return url_list




def pares_http_url(temp_url):
    """爬取网页源代码"""
    #设定headers
    request = urllib.request.Request(temp_url,headers=headersdatas.get_headers())
    ip_response = urllib.request.urlopen(request)
    html_content = ip_response.read().decode('utf-8')
    #print("结果：",html_content)
    return html_content
def main():
    #批量查询五页
    ip_url_datas = get_ip_url_list()
    #print(ip_url_datas)
    for http_url in ip_url_datas:


        ip_html_datas = pares_http_url(http_url)
        print(ip_html_datas)
        time.sleep(3)


if __name__ == '__main__':
    main()