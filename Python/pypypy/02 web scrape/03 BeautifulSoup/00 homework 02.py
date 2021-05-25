import requests
from bs4 import BeautifulSoup

print('---------Practise 1\n')
response = requests.get('http://books.toscrape.com/')
book_store_content = response.text
soup = BeautifulSoup(book_store_content, 'lxml')
items = soup.find('div', class_='side_categories')
book_type = items.find_all('a')
for item in book_type:
    print(item.string.strip())


print('\n---------Practise 2\n')
res = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
type_travel = res.text
soup = BeautifulSoup(type_travel, 'lxml')
items2 = soup.find_all('li')
for item2 in items2:
    print(item2)



# for item in items:
#     print(item)
#     print(type(item))
#     novel_type = item.find_all(a)
#     print(novel_type)


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