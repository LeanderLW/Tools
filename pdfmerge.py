import os
import re
from PyPDF2 import PdfMerger, PdfReader

# 使用正则表达式从文件名中提取以数字开头的部分作为排序键
def get_sort_key(filename):
    match = re.search(r'^\d+', filename)
    if match:
        return int(match.group())
    else:
        return filename

target_path = 'D:\Baidu\Download\极客时间\左耳听风'
wk_out_file_name = f"{target_path}\左耳听风.pdf"
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
sorted_pdf_list = sorted(pdf_lst, key=get_sort_key)


merger = PdfMerger()
wk_page_num = 0             # 记录每次合并一个pdf 文件后总页数
for item in sorted_pdf_list:   # 遍历输入目录下的所有pdf 文件
    if not item.startswith('.'):
        print('file item: ', item)
        wk_in_file_name = target_path + '\\' + item
        pdf_in = PdfReader(wk_in_file_name)  # 读取每个 pdf
        
        wk_title = item.split('.')[0]        # 目录标题
        merger.append(wk_in_file_name)       # 合并 pdf
        merger.add_outline_item(wk_title, wk_page_num, None)  # 添加目录项并指向合并的pdf的头页
        wk_page_num += len(pdf_in.pages)     # .pages  获得读进来的pdf的页数

merger.write(wk_out_file_name)
merger.close()