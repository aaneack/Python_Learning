import requests
# 引入BS库，下面的bs4就是beautifulsoup4
from bs4 import BeautifulSoup

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 把网页解析为BeautifulSoup对象
soup = BeautifulSoup(res.text,'html.parser')
# 查看soup的类型
print(type(soup))
# 打印soup
print(soup)


#使用 find
url = 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spder-men0.0.html'
res = requests.get (url)
print(f"\n{res.status_code}")
soup = BeautifulSoup(res.text,'html.parser')
# 使用find()方法提取首个<div>元素，并放到变量item里。
# item = soup.find_all('div')
# # 打印item的数据类型
# print(type(item))
# # 打印item
# print(item)

# 用find_all()把所有符合要求的数据提取出来，并放在变量items里
items = soup.find_all('div')
# 打印items的数据类型
print(f"\n{type(items)}")
# 打印items
print(items)

print("\n---------Practise 01")

# # 调用requests库
# import requests
# # 调用BeautifulSoup库
# from bs4 import BeautifulSoup
# # 返回一个response对象，赋值给res
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# # 把res的内容以字符串的形式返回
# html = res.text
# # 把网页解析为BeautifulSoup对象
# soup = BeautifulSoup( html,'html.parser')
# # 通过定位标签和属性提取我们想要的数据
# items = soup.find_all(class_='books')
# for item in items:
#     # 在列表中的每个元素里，匹配标签<h2>提取出数据
#     kind = item.find('h2')
#     # 在列表中的每个元素里，匹配属性class_='title'提取出数据
#     title = item.find(class_='title')
#     # 在列表中的每个元素里，匹配属性class_='info'提取出数据
#     brief = item.find(class_='info')
#     # 打印提取出的数据
#     print(kind,'\n',title,'\n',brief, '\n')
#     # 打印提取出的数据类型
#     print(type(kind),type(title),type(brief))

response = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = response.text
looking_for = BeautifulSoup( html, 'html.parser')
items = looking_for.find_all(class_='books')
for item in items:
    _type = item.find('h2')
    _title = item.find(class_='title')
    _info = item.find(class_='info')
    # print(f'\nType: {_type}\nTitle: {_title}\nInfo: {_info}')
    print(type(_type), type(_title), type(_info))
    print(f"\n{_type.text}\n{_title.text}\n{_title['href']}\n{_info.text}")