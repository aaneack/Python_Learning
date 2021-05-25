# 眼看要过年了，深夜食堂经营的不错，你打算给员工发奖金犒劳一下。请你定义函数，当输入员工姓名和工作时长两个参数，即可打印出该员工获得多少奖金。
#
# 发放奖金的要求如下：
#
# 工作时长不满六个月，发放固定奖金500元。
# 工作时长在六个月和一年之间(含一年)，发放奖金120元*月数（如8个月为960元）
# 工作时长在一年以上，发放奖金180元*月数 （如20个月为3600元）

# 我们可以定义两个函数，第一个函数功能为根据工作月数返回奖金额，第二个函数功能为打印出'该员工来了XX个月，获得奖金XXX元'。


# def month(month):
#     bonus = 0
#     if(0<month<=6):
#         bonus = 500
#     elif(6<month<=12):
#         bonus = month*120
#     elif(month>12):
#         bonus = month*180
#     return bonus
#
# def myprint(name,bonus):
#     print(name,bonus)
#
#
# if __name__ == '__main__':
#     actual_month = int(input('Please let me know how many monthes you have been joined our company?\nEnter here:'))
#     actual_name = input('Please let me know your name?')
#     bonus = month(actual_month)
#     myprint(actual_name,bonus)


def bonus(month):
    if month < 6:
        money = 500
        return money
    elif 6 <= month <= 12:
        money = 120 * month
        return money
    else:
        money = 180 * month
        return money

def info(name, month):
    gain = bonus(month)
    print('%s来了%s个月，获得奖金%s元' % (name, month, gain))

info('大聪',28)