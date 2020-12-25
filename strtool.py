import os
import fileinput

# 查看系统编码
# 当读取一个未知编码的文本时使用latin-1编码永远不会产生解码错误。 使用latin-1编码读取一个文件的时候也许不能产生完全正确的文本解码数据， 但是它也能从中提取出足够多的有用数据。同时，如果你之后将数据回写回去，原先的数据还是会保留的。
# import sys
# print(sys.getdefaultencoding())

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


with open('./output/out.text', 'wt', encoding='UTF-8') as f:
    for str_seted in str_set:
        f.write(str_seted)


# with open(fileinput.input(), 'rt', encoding='UTF-8') as f:
#     for line in f:
#         print(line, end='')