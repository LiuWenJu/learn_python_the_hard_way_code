#coding=utf-8
from sys import argv#引入相关模块

script, input_file = argv#输入文件为变量

def print_all(f):
    print f.read()#定义print_all函数

def rewind(f):
    f.seek(0)#定义rewind函数.（1）f.seek(p,0) 移动当文件第p个字节处，绝对位置

            #（2）f.seek(p,1) 移动到相对于当前位置之后的p个字节

            #（3）f.seek(p,2) 移动到相对文章尾之后的p个字节

def print_a_line(line_count, f):
    print line_count, f.readline()#定义print_a_line函数,打印行

current_file = open(input_file)#当前行即输入的文件

print "First let's print the whole file:\n"

print_all(current_file)#调print_all函数参数是current_file

print "Now let's rewind, kind of like a tape"

rewind(current_file)#调rewind函数,参数传的是current_file

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)#调print_a_line函数,传入current_line ,current_file

current_line = current_line + 1
print_a_line(current_line, current_file)#同上,current_line+ 1

current_line = current_line + 1
print_a_line(current_line, current_file)#同上,current_line + 1
