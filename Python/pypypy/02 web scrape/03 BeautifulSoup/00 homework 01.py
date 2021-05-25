import requests
from bs4 import BeautifulSoup

response_site = requests.get("https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/")
html = response_site.text
scrape_comment = BeautifulSoup( html, 'lxml')
items = scrape_comment.find_all('div', class_ = 'comment-content')
print(items)
print()

for item in items:
    print(item.p.string)




# response = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# html = response.text
# looking_for = BeautifulSoup( html, 'html.parser')
# items = looking_for.find_all(class_='books')
# for item in items:
#     _type = item.find('h2')
#     _title = item.find(class_='title')
#     _info = item.find(class_='info')
#     # print(f'\nType: {_type}\nTitle: {_title}\nInfo: {_info}')
#     print(type(_type), type(_title), type(_info))
#     print(f"\n{_type.text}\n{_title.text}\n{_title['href']}\n{_info.text}")