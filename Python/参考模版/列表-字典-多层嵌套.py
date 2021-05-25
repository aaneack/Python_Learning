# dict={'log_id': 5891599090191187877, 'result_num': 1, 'result': [{'probability': 0.9882395267486572, 'top': 205, 'height': 216, 'classname': 'Face', 'width': 191, 'left': 210}]}
#
# # 访问dict下的result列表的值：
# print(dict['result'][0]['top'] )
# # dict下的result列表的第一个值（字典）的top内容
#
# # 也可以使用临时变量:
# dict1=dict['result']
# print(dict1[0]['probability'])


c = {
        "forchange":
        [
            {"name": "backer", "age": 5},
            {"name": "willie", "age": 18},
            {"name": "penny", "age": 20},
        ]

    }

print(c["forchange"][0]["name"])
