print("hello,world")
'''
str = '何飞阳正在学习Python'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:])
print(str + "你好")
print(str+"\n"+"nihao" )

information = input('\n\n按下enter推出')
print(information)

import sys
print("===========python import sys mode===========")
print("命令行参数为：")
for i in sys.argv:
    print(i)
print("\n python 路径为", sys.path)

x = "朱蓉可能是个傻子把"
sys.stdout.write(x + '\n')

print('hhh',end=' ')#不换行输出
print('朱蓉真的是个傻子')
'''
from sys import argv,path
print("==========python从sys模块导入特定成员arg，path===========")
print("path:",path)

111
222