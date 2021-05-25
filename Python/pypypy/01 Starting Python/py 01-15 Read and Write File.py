file1 = open('/Users/aaneack/Downloads/123.txt', 'w', encoding="utf-8")
file1.write("Nic's first Python writing file\n")
file1.write("Try again!\n")
file1.close()

file1 = open('/Users/aaneack/Downloads/123.txt', 'r', encoding="utf-8")
filecontent1 = file1.read()
print(filecontent1)
file1.close()

file1 = open('/Users/aaneack/Downloads/123.txt', 'a', encoding="utf-8")
file1.write('Add some new words\n')
file1.write('Add more words\n')
file1.close()

file1 = open('/Users/aaneack/Downloads/123.txt', 'r', encoding="utf-8")
filecontent1 = file1.read()
print(filecontent1)
file1.close()

# homework
file2 = open('/Users/aaneack/Downloads/score.txt', 'w', encoding="utf-8")
file2.write('罗恩 23 35 44\n')
file2.write('哈利 60 77 68 88 90\n')
file2.write('赫敏 97 99 89 91 95 90\n')
file2.write('马尔福 100 85 90\n')

file2 = open('/Users/aaneack/Downloads/score.txt', 'r', encoding="utf-8")
filecontent2 = file2.read()
print("Score:\n" + filecontent2)
file2.close()

file3 = open('/Users/aaneack/Downloads/score.docx', 'w', encoding="utf-8")
file3.write('罗恩 23 35 44\n')
file3.write('哈利 60 77 68 88 90\n')
file3.write('赫敏 97 99 89 91 95 90\n')
file3.write('马尔福 100 85 90\n')

file3 = open('/Users/aaneack/Downloads/score.docx', 'r', encoding="utf-8")
filecontent3 = file3.read()
print("Score:\n" + filecontent3)
file3.close()

file4 = open('/Users/aaneack/Downloads/score.xlsx', 'w', encoding="utf-8")
file4.write('罗恩 23 35 44\n')
file4.write('哈利 60 77 68 88 90\n')
file4.write('赫敏 97 99 89 91 95 90\n')
file4.write('马尔福 100 85 90\n')

file4 = open('/Users/aaneack/Downloads/score.xlsx', 'r', encoding="utf-8")
filecontent4 = file4.read()
print("Score:\n" + filecontent4)
file4.close()

file2 = open('/Users/aaneack/Downloads/score.txt', 'r', encoding="utf-8")
file_lines = file2.readlines()
file2.close
print(file_lines)

for i in file_lines:
    print(i)

file2 = open('/Users/aaneack/Downloads/score.txt', 'r', encoding="utf-8")
file_lines = file2.readlines()
file2.close
print(file_lines)

for i in file_lines:
    data = i.split()
    print(data)

# 求和

for i in file_lines:
    data = i.split()
    sum = 0
    for score in data[1:]:
        sum = sum + int(score)
    result = data[0] + str(sum)
    print(result)

#把成绩写入一个空的列表

final_scores = []

for i in file_lines:
    data= i.split()
    sum = 0
    for score in data[1:]:
        sum = sum +int(score)
    result = data[0] + str(sum)+'\n'
    final_scores.append(result)

winner = open('/Users/aaneack/Downloads/score.txt', 'w', encoding="utf-8")
winner.writelines(final_scores)
winner.close()