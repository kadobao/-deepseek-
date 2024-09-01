import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import urllib3
urllib3.disable_warnings()

# 文件路径
deepseek_endpoints = r"C:\Users\cf\Downloads\deepseek_endpoint.txt"

# 打开文件
with open(deepseek_endpoints, "r", encoding="utf-8") as file:
    # 逐行读取文件
    lines = file.readlines()


output_file = r"C:\Users\cf\Downloads\deepseek_endpoint1.txt"


def verify_url(url):
    try:
        url = url.strip()
        # 发送HTTP请求
        response = requests.get(url, verify=False, timeout=30)

        # 检查响应状态码是否为200
        if response.status_code == 200:
            # 解析HTML内容
            soup = BeautifulSoup(response.text, 'lxml')

            # 查找包含目标文本的<p>标签
            p_tag = soup.find('p')

            target_text = p_tag.get_text()

            if p_tag:
                target_text = p_tag.get_text()
                print(target_text)
                # 检查目标文本是否包含 "deepseek-free-api已启动！"
                if "deepseek-free-api已启动！" in target_text:
                    with open(output_file, "a", encoding="utf-8") as out_file:
                        out_file.write(url + "\n")
                    return url
    except Exception as e:
        print(f"{url}")
    return None





with ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(verify_url, lines)
