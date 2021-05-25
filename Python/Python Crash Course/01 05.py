# 5.1
cars =["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# 5.2.3
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("\nHold the anchovies!")


print("\n5.2.5--------[if and]\n")

age_0 = 22
age_1 = 18
print(f"age_0 >= 21 and age_1 > 21 = {age_0 >= 21 and age_1 > 21}\n")

age_1 = 22
print(f"age_0 >= 21 and age_1 > 21 = {age_0 >= 21 and age_1 > 21}\n")

# 简化版本
print(f"简化版本 (age_0 >= 21) and (age_1 >= 21) = {(age_0 >= 21) and (age_1 >= 21)}")


print("\n--------[if or]\n")
age_0 = 22
age_1 = 18
print(f"age_0 >= 22 or age_1 >= 18 = {age_0 >= 21 or age_1 >= 21}\n")

age_0 = 18
print(f"age_0 >= 18 or age_1 >= 18 = {age_0 >= 21 or age_1 >= 21}\n")

print("5.2.6--------检查特定值是否包含在列表中\n")
requested_toppings = ["mushroom", "onions", "pineapple"]
print("Does mushroom in the toppings?")
print("mushroom" in requested_toppings)

print("\nDoes pepperoni in the toppings?")
print("pepperoni" in requested_toppings)

print("5.2.7--------检查特定值是否不包含在列表中\n")
banned_user = ["andrew", "carolina", "david"]
user = "marrie"

if user not in banned_user:
    print(f"{user.title()}, you can post a response if you wish.")

print("\n5.2.8--------布尔表达式\n")
game_active = True
can_edit = False

print("\n--------Practise 5-1\n")
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

print("\n5.3.3--------if-elif-else结构\n")
# 练习 - 4岁以下免费，4～18岁收费25美元，18岁（含）以上收费40美元
age_3 = 5
if age_3 < 4:
    print("Your admission cost is free.")
elif age_3 < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

print("\n5.3.3--------简化代码\n")
age_4 = 12
if age_4 < 4:
    price = 0
elif age_4 < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")

print("\n5.3.4--------添加老年人65岁半价优惠\n")
age_4 = 65
if age_4 < 4:
    price = 0
elif age_4 < 18:
    price = 25
elif age_4 < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")

print("\n5.3.5--------添加老年人65岁半价优惠，省略else，python可省略else\n")
age_4 = 65
if age_4 < 4:
    price = 0
elif age_4 < 18:
    price = 25
elif age_4 < 65:
    price = 40
elif age_4 >= 65:
    price = 20
print(f"Your admission cost is ${price}")

print("\n5.3.6--------测试多个条件\n")
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
# pepperoni is not in the requested_toppings, so it won't be printed.
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
print("\nFinished making your pizza!\n")

print("Compare if-elif-else, the result only choose the first matches condition.")
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
print("Finished making your pizza!\n")

print("\nIf you only wanna carry out 1 condition, use if-elif-else. \nIf you'd like to carry our multiple condition, use if-if-if-if\n")

# print("--------Practise 5-3 5-4 5-5\n")
# alien_color = input("Please let me know which color of alien you've killed?\n(green, yellow or red): ")
# if alien_color == "green":
#     print("You got 5 score.")
# elif alien_color == "yellow":
#     print("You got 10 score.")
# elif alien_color == "red":
#     print("You got 15 score.")
# else:
#     print("Please enter the correct alien color.")

# print("\n--------Practise 5-6\n")
# the_age = int(input("Please enter the age: "))
# if 0 <= the_age < 2:
#     print(f"{the_age} year(s) old is a newborn baby.")
# elif 2 <= the_age < 4:
#     print(f"{the_age} years old is an infant.")
# elif 4 <= the_age < 13:
#     print(f"{the_age} years old is a child.")
# elif 13 <= the_age < 20:
#     print(f"{the_age} years old is a teenager.")
# elif 20 <= the_age < 65:
#     print(f"{the_age} years old is an adult.")
# elif 65 <= the_age < 130:
#     print(f"{the_age} years old is a senior citizen.")
# else:
#     print("Please enter correct age.")

# print("\n--------Practise 5-7\n")
# sell_fruits = ["apple", "banana", "avacado"]
# wanna_buy_fruit = input("Please let me know what fruit would you like to buy? : ")
# if wanna_buy_fruit in sell_fruits:
#     print(f"Sure, I will get you {wanna_buy_fruit} now.")
# else:
#     sell_fruits.append(wanna_buy_fruit)
#     print(f"I am sorry, we don't have {wanna_buy_fruit} today. Please come back tomorrow.")
# print(sell_fruits)

print("\n5.4.1--------检查特殊元素\n")
requested_toppings = ["mushroom", "onions", "pineapple"]
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# 如果某种pizza材料用完了
for requested_topping in requested_toppings:
    if requested_topping == "mushroom":
        print("\nSorry, we are outta mushroom.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!\n")

# 空列表
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!")
else:
    print("\nAre you sure you want plain pizza.")


print("\n5.4.3--------使用多个列表\n")
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "cake", "banana", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

print("\n--------Practise 5-9\n")

#users = ["aaneack", "nic", "chen", "zhengxi", "aa"]
users = []
if users:
    for user in users:
        if user == "aaneack":
            print(f"Hello admin {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("\n--------Practise 5-10\n")


current_users = ["aaneack", "nic", "chen", "zhengxi", "aa"]
new_users = ["aaneack", "eric", "wings", "zhengxi", "aa"]
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"You can't use '{new_user}' as your user name.")
    else:
        print(f"Your user name '{new_user}' is available.")

print("\n--------Practise 5-11\n")
numbers = range(1,10)
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")