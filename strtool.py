import os

# 文件路径
file_list = ['./input/sys_dict_item.sql', './input/new4.txt']
# 搜索关键字
keyword = ['BUS-RelZZD', '']

lines = 0
str_list = []
str_set = set()

with open(file_list[1], encoding='UTF-8') as f:
    read_data = f.readline()
    for line in f:
        # 先放入列表
        str_list.append(line)
        # 搜索
        if keyword[0] in line:
            lines = lines + 1
            print(line, end='')
# 去重
str_set = set(str_list)
for str_seted in str_set:
    print(str_seted)

print("根据关键字搜索到", lines, "条数据")
print("去重之后", len(str_set), "条")
