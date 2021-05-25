magicians = ["david" , "taylor" , "britney", "beyonce"]
for magician in magicians:
    print(f"{magician.title()}, your trick is incredible.")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone, it was a great magic show.")

print("\n---------------Practise 4-1\n")
pizza_type = ["pepperoni pizza" , "hawaii pizza", "margherita pizza"]
for pizza in pizza_type:
    print(f"I love {pizza} soooo much!\n")
print("Pizza is my favorite!")

print("\n---------------Practise 4-2\n")
pets = ["cat" , "dog" , "pig"]
for pet in pets:
    print(f"A {pet} would make a great pet.")
print("Any of these animals would make a great pet.")

# range括号内，取左不取右
for value in range(-10,10):
    print(value)

print("\n")

# range中设置三个参数时候，即为指定步长。 1为starter，10为end，步长为3。
for value2 in range(1,10,3):
    print(value2)

print("\n")

# list()将range()的结果直接转换为列表。
numbers1 = list(range(6))
print(numbers1)

print("\nrange制作平方列表")
# 使用range创建平方列表1，基础篇
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print("\n简洁平方列表")
# 使用range创建平方列表2，简洁篇
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

print("\n4.3.3 对数字列表执行简单对统计计算")
digits = [1, 2, 3, 4, 5, 5, 6, 7, 8, 10]
num1 = min(digits)
num2 = max(digits)
num3 = sum(digits)
print(f"min = {num1}\nmax = {num2}\nsum = {num3}")

print("\n4.3.3 对数字列表执行简单对统计计算")

squares = [value ** 2 for value in range(1,11)]
print(squares)

print("\nPractise--------- 4-3")
for counting20 in range(21):
    print(f"Counting down {counting20}")

print("\nPractise--------- 4-4")
list_million = range(1,31)
for i in list_million:
    print(i)

print("\nPractise--------- 4-5")
print(f"In the list on 1~30\nMax = {max(list_million)} Min = {min(list_million)} Sum = {sum(list_million)}")

print("\nPractise--------- 4-6")
odd_numbers = [odd_number for odd_number in range(1,20,2)]
print(odd_numbers)

print("\nPractise--------- 4-7")
_3times = []
for _3time in range(3,31):
    if _3time%3 == 0:
        _3times.append(_3time)
print(_3times)

_3time = ([_3time for _3time in range(3,31) if _3time % 3 == 0])
print(_3times)

print("\nPractise--------- 4-8")
cube_1 = [1,2,3,4,5,6,7,8,9,10]
_3cube = []
for cube in cube_1:
    _3cube.append(cube**3)
print(_3cube)

print("\nPractise--------- 4-9")
cube_1 = [cube ** 3 for cube in range(1,11)]
print(cube_1)

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli")
friend_foods.append("pasta")

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nPractise--------- 4-10")
my_things = ["macbook pro", "washing machine", "sofa", "kettle", "rowing machine"]
print(f"the first three items in the list are: {my_things[:4]}")
print(f"Three items from the middle of the list are: {my_things[1:4]}")
print(f"The last three items in the list are: {my_things[-3:]}")

print("\nPractise--------- 4-11")
my_pizzas = ["pizza1", "pizza2", "pizza3"]
print(f"The original my pizzas are: \n{my_pizzas}")

friend_pizzas = my_pizzas[:]
my_pizzas.append("pizza4")
friend_pizzas.append("pizza5")

print(f"My favorite pizzas are: \n{my_pizzas}.")
print(f"My friend's favorite pizzas are: \n{friend_pizzas}.")

print(f"My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print(f"\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

print("\nPractise--------- 4-12")


print("\nPractise--------- 4-12\n")
previous_dishes = ("wings", "salad", "pasta", "cheese cake")
new_dishes = ("chips", "salad", "pasta", "cheese cake")
print(f"Our buffet is included below dishes:")
for dish in new_dishes:
    print(dish)
