bicycles = ["trek" , "cannodale" , "redline", "specialized"]
message = f"My first bicycle was a {bicycles[0].title()}."
print(bicycles[0].title())
print(bicycles[-1].title())
print(bicycles[-2].title())
print(message)


print("\n----------Practise 3-1\n")
names = ["Aaneack","Nic","Aa","alex","Eric","Wings"]
message_3_1 = ", how are you doing?"
print(names)
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())

print("\n")

print(f"{names[0].title()}{message_3_1}")
print(f"{names[1].title()}{message_3_1}")
print(f"{names[2].title()}{message_3_1}")
print(f"{names[3].title()}{message_3_1}")
print(f"{names[4].title()}{message_3_1}")
print(f"{names[5].title()}{message_3_1}")


print("\n----------Practise 3-2\n")
message_3_2 = "I would like to have a"
print(f"I am {names[0].title()}, {message_3_2} {bicycles[0].title()}.")

print("\n----------Practise 3-3\n")
print(bicycles)

# list.append 添加元素
bicycles.append("sandy")
print(bicycles)
print(bicycles[-1])

# list[1] = "String" 指定列表元素，替换元素
bicycles[-1] = "mandy"
print(bicycles)
print(bicycles[-1])

# list.insert(number/location, 元素) 插入元素
bicycles.insert(5, "candy")
print(bicycles)

# del list(number/location) 删除元素
del bicycles[5]
print(bicycles)

# list.pop 删除元素
popped_bicycle = bicycles.pop(0)
print(f"This is popped {popped_bicycle}")

print("del和.pop 若后续不需要元素即可使用del来删除，若后续可能使用删除的元素的话，可以使用.pop\n")

# .remove(), 用于不知道列表位置，知道元素名字的移除。
not_bicycle = "mandy"
bicycles.remove(not_bicycle)
print(f"Mandy is not a bicyble brand, removed {not_bicycle.title()}")
print(bicycles)

print("\n----------Practise 3-4\n")

dinner_list = ["Eric", "Wings", "Rene", "Charlie"]
message_3_4 = f"I would like to invite {dinner_list} to have dinner with me."
print(message_3_4)

print("\n----------Practise 3-5\n")
popped_person = dinner_list.pop(3)
print(f"At last I decide that not to invite {popped_person}. And list now is {dinner_list}")

print("\n----------Practise 3-6\n")

dinner_list.insert(0, "Frank")
print(f"Added {dinner_list[0]} to the list.")

dinner_list.insert(1, "Driver")
print(f"Added {dinner_list[1]} to the list.")

dinner_list.append("Niangniang")
print(f"Added {dinner_list[5]} to the list.")
print(f"Here is the current list {sorted(dinner_list)}")

print("\n----------Practise 3-7\n")
print(f"Current dinner list {dinner_list}")
print("Use del command to delete element")
del dinner_list[0]
print(f"Deleted [0], del result {dinner_list}")

print(f"\nCurrent dinner list {dinner_list}, I will use remove command below.")
a = dinner_list.remove("Wings")
print(f"Wings was removed. Here is the remove command result {dinner_list}")

print(f"\nCurrent dinner list {dinner_list}, I will use pop command below.")
popped_dinner_list = dinner_list.pop()
print(f"I popped the list, let's check it {sorted(dinner_list)}. I have popped {popped_dinner_list} from the list.\nDo you see the difference from the 3 ways to delete the element from the list?")

dinner_list.sort()
print(dinner_list)

dinner_list.sort(reverse=True)
print(dinner_list)