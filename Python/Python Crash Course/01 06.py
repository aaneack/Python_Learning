print("----------6.1 一个简单的字典\n")

alien_0 = {"color": "green", "point": 5}
print(alien_0["color"], alien_0["point"])

#
print("\n----------6.2.1 访问字典中的值\n")

kill_alien = alien_0["color"]
new_point = alien_0["point"]

print(f"You've killed a {kill_alien} alien and get 5 points!")

#
print("\n----------6.2.2 添加键值\n")
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

#
print("\n----------6.2.4 修改字典中的值\n")

alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}.")

alien_0 = {"color": "yellow"}
print(f"The alien is {alien_0['color']}.\n")

# Game
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Orginal x_position: {alien_0['x_position']}")
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New x_position: {alien_0['x_position']}")

#
print("\n----------6.2.5 删除键值对\n")
alien_0 = {"color": "green", "point": 5}
print(alien_0)

# del删除的键对会永远消失
del alien_0["point"]
print(alien_0)


#
print("\n----------6.2.6 由类似对象组成的字典\n")
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

#
print("\n----------Practise 6-1\n")
wing = {"first name": "yi", "last name": "zeng", "age": 29, "home town": "loudi", "city": "shenzhen"}
print(f"Wing's first name is {wing['first name'].title()} and his last name is {wing['last name'].title()}.")
print(f"He was born in {wing['home town'].title()} city, but he is living in {wing['city'].title()} with me at the moment!")

print("\n----------Practise 6-2\n")
fav_numbers = {
    "wing": 111,
    "jon": 0.5,
    "eric": 111111,
    "rene": 0.5,
    "lu": 1,
    "frank": 1,
}
his_fav_num = input("Whose favorite number do you wanna know?\nEnter a name here(Wing / Jon / Eric / Rene / Lu / Frank/): ")
his_fav_num = his_fav_num.lower()
print(f"{his_fav_num.title()}'s favorite number is {fav_numbers[his_fav_num]}.")

print("\n----------Practise 6-3\n")
python_language = {
    "print" : "print命令可以打印你想打印的代码。",
    "list" : "list可以储存各种元素，并且元素可以被替换。",
    "tuples":"tulpes和list有点像，可以储存各种元素，但是使用()。tuples的元素不可以被替换。",
}
for key, value in python_language.items():
    print(f"{key}: {value}\n")

#
print("\n----------6.3 遍历字典\n")
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
 }

for k, v in user_0.items():
    print(f"\nkey: {k}")
    print(f"value: {v}")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name, favorite_language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {favorite_language}.")