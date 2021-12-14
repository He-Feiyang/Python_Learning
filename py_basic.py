print("python learning:")
print("=================================================================================================")
'''
if True:
    print("hope you have a happy journy!")
else:
    print("false")

#多行语句
item_1 = 1
item_2 = 2
item_3 = 3
total = item_1 + \
        item_2 + \
        item_3 
#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \


#单引号和双引号一样，都表示字符串
word = 'this is string, you can print it.\n'
sentence = "this also is string"
print( word, sentence)
'''
#三个引号用来表示多行字符串
#paragraph = '''this is a paragraph
#you can write so many words in 
#different lines'''
#print(paragraph)

'''
str = '何飞阳正在学习Python'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:])
print(str + "你好")
print(str+"\n"+"nihao" )


#输入
information = input('\n\n按下enter退出')
print(information)
'''
'''
import sys
print("===========python import sys mode===========")
print("命令行参数为：")
for i in sys.argv:
    print(i)
print("\n python 路径为", sys.path)

x = "朱蓉可能是个傻子把"
sys.stdout.write("\n" + x + '\n')#换行输出

print('hhh',end=' ')#不换行输出
print('朱蓉真的是个傻子')

from sys import argv,path
print("==========python从sys模块导入特定成员arg，path===========")
print("path:",path)
'''
'''
#python中变量就是变量，没有类型，我们通常所说的类型是指内存中对象的类型
counter = 100      #int
miles = 12.3       #float
name = "hefeiyang" #string
'''

'''
print("python中的6个标准数据类型：\n Number  string  List  Tuple  Set  Dictionary")
print("其中：\n 不可变数据有：\n    Number    string    Tuple\n 可变数据类型有：\n    List    Dictionary    Set")

print(type(name),type(miles),type(counter))#type()用来查询数据类型
print(isinstance(name,str))
'''
'''
#isinstance与type()的区别：isinstance会认为子类是一种父类类型，type不会
class A:
    pass

class B(A):
    pass

typea = isinstance(A(),A)
typeb = isinstance(B(),A)
typec = type(A())
print(typea,typeb,typec)

if isinstance(A(),A) == type(A()):
    print("equal")
else:
    print("not equal")

JudgeSubType = issubclass(bool, int)
print(JudgeSubType)

print(5/2) #除法，返回浮点数
print(5//2)#除法，只取整数部分
print(2**3)

word = "python"
print(word[-1])
print(word[0])
print(word[-0])
print(word[0:-1])
#字符串的两种索引方式：从左往右以0开始，从右往左-1开始
'''

'''
list = ["hfy ", 123, "lalala", 77.77]
tinylist = ["this is ", 22.22, "tiny list"]
print(list)
print(list[1])
print(list[1:3])
print(list+tinylist)
'''

'''
def reverseWords(input):
    inputWords = input.split()

    inputWords = inputWords[-1: :-1]

    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = "i like runoob"
    rw = reverseWords(input)
    print(rw)
'''
#tuple与list类似，区别在于tuple中的元素不能修改
tuple = ("hefeiyang",)












