# 引入requests库
import requests

res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# 打印变量res的响应状态码，以检查请求是否成功
print(res.status_code)


#下载书，方法1
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# 把Response对象的内容以字符串的形式返回
novel = res.text
# 创建一个名为《三国演义》的txt文档，指针放在文件末尾，追加内容
k = open('《三国演义》.txt','a+')
# 写进文件中
k.write(novel)
# 关闭文档
k.close()


#下载图片
url2 = "https://res.pandateacher.com/2018-12-18-10-43-07.png"
# 发出请求，并把返回的结果放在变量res中
res2 = requests.get(url2)
# 把Reponse对象的内容以二进制数据的形式返回
pic = res2.content
# 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 图片内容需要以二进制wb读写。你在学习open()函数时接触过它。
photo = open('ppt.jpg','wb')
# 获取pic的二进制内容
photo.write(pic)
# 关闭文件
photo.close()



# 下载《三国演义》第一回，我们得到一个对象，它被命名为res
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# 定义Response对象的编码为gbk
#res.encoding='gbk'
res.encoding='utf-8'
# 把Response对象的内容以字符串的形式返回
novel=res.text
# 打印小说的前800个字
print(novel[:800])