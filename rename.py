import os
import os.path


dir_path = 'D:\\Downloads\\Video'
'''文件目录'''

target_str = ['233', '322']
'''要删除的字符'''

filename_list = os.listdir(dir_path)

for filename in filename_list:
    refilename = ''
    for s in target_str:
        if s in filename:
            refilename = filename.replace(s, '')
    filename = os.path.join(dir_path, filename)
    refilename = os.path.join(dir_path, refilename)
    try:
        os.rename(filename, refilename)
    except:
        print(refilename, "文件已存在")
