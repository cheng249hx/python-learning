#第一个python文件

# 一、基本数据类型
var1 = "Hello World"            #字符串、str
var2 = "I want to see the word"
var3 = 1                        #整型、int
var4 = 3.14                     #浮点型、float
var5 = True                     #bool类型
var6 = False
var7 = None                     #空型、None type
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)
print(var7)
print(var1, var2, var3, var4, var5, var6, var7)

#二、标识符（变量、函数等的名称）、命名规则与C语言一致
#python中的变量没有类型，一个变量可以存储不同类型的数据，但尽量不要这么做

#三、定义字符串的三种方式
#单引号定义
var8 = 'What is your name?'
#双引号定义
var9 = "My name is Cheng Huaxiang."
#三引号定义（多行字符串）
var10 = """
Python学习
    尝试定义多行字符串。
"""
print(var8)
print(var9)
print(var10)

#四、字符串的拼接
s1 = "人生苦短"
s2 = "我用Python"
name = "程华祥"
age  = 20
pro = "软件工程"

#使用'+'号来拼接字符串
print("他说："+s1+","+s2)
# age是int类型，不能直接拼接，需要先将其转换为str类型,使用str(...)
print("我的名字是"+name+"，今年"+str(age)+"，专业是"+pro)

#字符串的格式化
#使用占位符格式化
print("他说：%s,%s"%(s1,s2))
print("我的名字是%s,今年%s，专业是%s"%(name,age,pro))
#使用f"内{变量/表达式}”的形式快速完成格式化
print(f"他说：{s1},{s1}")
print(f"我叫{name},我今年{age}，专业是{pro}")

#五、使用type(...)查看数据的实际类型
#具体语法 type(要查看的数据)
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var6))
print(type(var7))
print(type(var8))
print(type(var9))
print(type(var10))

#六、使用isinstance()检查数据是否为指定的类型，返回值为bool值
#具体语法为 isinstance(数据，类型)
print(isinstance(var1, str))
print(isinstance(var1, int))
print(isinstance(var1, float))

#七、使用input语句(函数)获取键盘输入的数据
#使用方法 s = input("提示信息"),注意括号内的引号
# var11 =input("请输入：")
# print("var11的值为：",var11)
# #通过input()输入的数据均为字符串（str）类型
# print("var11的类型为",type(var11))
# #若需要其他类型的数据则需要强制转换，如：
# var12 = int(input("请输入整数:"))
# print("var12的值为：",var12)
# print("var12的类型为：",type(var12))

#八、类型转换
# int(...)      转换为int型
# float(...)    转换为float型
# str(...)      转换为str型
# bool(...)     转换为bool型

#九、算数运算符
# 1，加     +     eg. 1 + 2 = 3
# 2，减     -     eg. 2 - 1 = 1
# 3，乘     *     eg. 1 * 2 = 2
# 4，除     /     eg. 10 / 5 = 2.0  结果是小数
# 5，整除   //     eg. 10 // 3 = 3   结果是整数
# 6，取模   %      eg. 10 % 3 = 1
# 7，幂指数 **      eg. 10 ** 3 = 1000  10的3次方

print(1 + 2)
print(2 - 1)
print(1 * 2)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

#十、赋值运算符
#   =
#   +=
#   -=
#   *=
#   /=
#   //=
#    %=
#   **=
#以上运算符规则与C语言类似

# 十一、可以用bool()函数查看布尔值
print(bool(var3))
print(bool(var5))
print(bool(var7))

# 十二、元组类型
# 元组可以保存任意数量，任意类型的元素，但这些元素不能被修改
# python中通常使用小括号创建元组，元组中元素使用英文逗号隔开
#示例如下
var11 = (1, 4.5, "python")
print(var11)

# 十三、列表类型
# 列表可以保存任意数量，任意类型的元素，且这些元素可以被修改
# python中通常使用中括号创建列表，列表中元素使用英文逗号隔开
#示例如下
var12 = [1, 2, 3]
print(var12)

# 十四、集合类型
# 集合可以保存任意数量，任意类型的元素，但这些元素是无序且唯一的
# 在python中一般使用大括号创建集合
var13 = {"apple", "banana", 1}
print(var13)

# 十五、字典类型
# 字典可以保存任意数量的元素，元素类型是“key：value”形式的键对值

# sum = 0
# for i in range(100):
#     if (i % 10):
#         continue
#     sum += i
# print(sum)

Python = 1
print(Python)