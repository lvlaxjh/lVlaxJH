import requests
from bs4 import BeautifulSoup
url = 'https://app.bupt.edu.cn/buptys/wap/default/index'
print(url)
response = requests.get(url, timeout=5)
soup= BeautifulSoup(response.text, 'html.parser')
