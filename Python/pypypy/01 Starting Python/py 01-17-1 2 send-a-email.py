import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = '89650578@qq.com'
password = 'xxqgwnujtpxbbhib'
#to_addr1 = 'aaneack@163.com'
#to_addr2 = 'aaneack@outlook.com'
smtp_server = 'smtp.qq.com'
text1 = '''I'd like to try the last time on python to send multiple addresses!'''
msg = MIMEText(text1, 'plain', 'utf-8')


# Single email
# msg['From'] = Header(from_addr)
# msg['To'] = Header(to_addr1)
# msg['Subject'] = Header("I am testing multiple email addresses")

# Multiple email

msg["From"] = Header(from_addr)
msg["To"] = Header(",".join(to_addrs1))
msg["Subject"] = Header("Last try")


to_addrs = []
while True:
    a=input('请输入收件人邮箱：')
    #输入收件人邮箱
    to_addrs.append(a)
    #写入列表
    b=input('是否继续输入，n退出，任意键继续：')
    #询问是否继续输入
    if b == 'n':
        break

print(to_addrs)

server = smtplib.SMTP(smtp_server, 587)
server.connect(smtp_server, 587)
server.login(from_addr, password)
# pay attention on to_addr(s)1 if send email to multiple receiver
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()



# Multiple email address uses the command .join
# a=['d','o','g']
# b=','
# print(b.join(a))
# c='-'
# print(c.join(a))


# # smtplib 用于邮件的发信动作
# import smtplib
# from email.mime.text import MIMEText
# # email 用于构建邮件内容
# from email.header import Header
# # 用于构建邮件头
#
# # 发信方的信息：发信邮箱，QQ 邮箱授权码
# from_addr = input('请输入登录邮箱：')
# password = input('请输入邮箱授权码：')
#
# # 收信方邮箱
# to_addrs = []
# while True:
#     a=input('请输入收件人邮箱：')
#     to_addrs.append(a)
#     b=input('是否继续输入，n退出，任意键继续：')
#     if b == 'n':
#         break
#
# # 发信服务器
# smtp_server = 'smtp.qq.com'
#
# # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
# text='''亲爱的学员，你好！
# 我是吴枫老师，能遇见你很开心。
# 希望学习Python对你不是一件困难的事情！
#
# 人生苦短，我用Python
# '''
# msg = MIMEText(text,'plain','utf-8')
#
# # 邮件头信息
# msg['From'] = Header(from_addr)
# msg['To'] = Header(",".join(to_addrs))
# msg['Subject'] = Header('python test')
#
# # 开启发信服务，这里使用的是加密传输
# server = smtplib.SMTP_SSL(smtp_server)
# server.connect(smtp_server,465)
# # 登录发信邮箱
# server.login(from_addr, password)
# # 发送邮件
# server.sendmail(from_addr, to_addrs, msg.as_string())
# # 关闭服务器
# server.quit()