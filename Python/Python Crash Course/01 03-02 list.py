cars = ["bmw","toyota","audi","subaru"]

print(f"Orginal list {cars}")

# sorted(), 临时排序
print(f"\nsorted() the list, {sorted(cars)}")

# list.reverse() 永久倒序，再reverse一次可返回原来list排序
cars.reverse()
print(f"\nReverse the list, {cars}")

cars.reverse()
print(f"\nthe second time reverse the list {cars}")

# list.sort() 永久排序
cars.sort()
print(f"\nsort() the list, {cars}")

# len(list) 可查询list中的元素数量
print(f"\nlen(list) the list, there is / are {len(cars)} element(s) in the list.")

print("---------Practise 3-8\n")

wanna_visit_spots = ["xizang", "xinjiang", "dunhuang","france", "germany", "spain", "italy", "portugal", "sweden", "switzerland", "netherlands", "norway", "ice land", "alaska", "agentina"]
print(f"Original list where I wanna visit \n{wanna_visit_spots}\n")

print(f"sorted the Original list where I wanna visit \n{sorted(wanna_visit_spots)}\n")

wanna_visit_spots.reverse()
print(f"Reversed the original list where I wanna visit \n{wanna_visit_spots}\n")

wanna_visit_spots.reverse()
print(f"2nd time reversed the original list where I wanna visit \n{wanna_visit_spots}\nIt goes back to the orginal list.\n")

wanna_visit_spots.sort()
print(f"1st time to sort the original list where I wanna visit \n{wanna_visit_spots}\n")

wanna_visit_spots.sort(reverse=True)
print(f"2nd time to sort the original list where I wanna visit \n{wanna_visit_spots}\n")

for paradise in wanna_visit_spots:
    print(paradise)