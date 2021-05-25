def tree(Height):
    print('Merry Christmas!')
    for i in range(Height):
        print((Height-i)*2*' '+'o'+ i*'~x~o')
        print(((Height-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')
    return "\n"
print(tree(10))

def menu(appetizer,course,dessert='绿豆沙'):
    print('一份开胃菜：'+appetizer)
    print('一份主食：'+course)
    print('一份甜品：'+dessert+'\n')


menu('话梅花生','牛肉拉面')
menu('话梅花生','牛肉拉面','银耳羹')
menu('话梅花生','牛肉拉面')

def menu(*barbeque):
    print(barbeque)

menu('烤鸡翅','烤茄子','烤玉米')
#这几个值都会传递给参数barbeque

def menu(appetizer, course, *barbeque, dessert='绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主菜：' + course)
    print('一份甜品：' + dessert)
    for i in barbeque:
        print('一份烤串：' + i)


menu('话梅花生', '牛肉拉面', '烤鸡翅', '烤茄子', '烤玉米')

def face(name):
    return name + '的脸蛋'
#该函数返回字符串'XXX的脸蛋'
def body(name):
    return name + '的身材'
#该函数返回字符串'XXX的身材'

face('李若彤')
body('林志玲')
#分别调用face()和body()函数

print('我的梦中情人：'+face('李若彤') +' + ' + body('林志玲'))
#将返回值拼接并打印出来

def face(name):
    return name + '的脸蛋'
def body(name):
    return name + '的身材'
def main(dream_face,dream_body):
    return '我的梦中情人：' + face(dream_face) + ' + ' + body(dream_body)

print(main('李若彤','林志玲'))
print(main('新垣结衣','长泽雅美'))

def pet(pet_type, pet_name):
    print(f"I have a {pet_type}.\nAnd her name is {(pet_name).title()}.")
pet("dog", "seth")

def lover(name1, name2):
    face = f"{(name1).title()}'s face"
    body = f"{(name2).title()}'s body"
    return face, body
a = lover('jon kortajarena', 'rick martin')
print(a)
print(f"\nMy dream lover has {a[0]} and {a[1]}.\n")

#第一个函数
def fun():
    a ='I am coding'
print(fun())

#第二个函数
def fun():
    a='I am coding'
    return a
print(fun())
#1不返回值 不打印，2打印。


def number1(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 'The numbers are equal.'
print(f"\n{number1(99**2, 8888)}")






