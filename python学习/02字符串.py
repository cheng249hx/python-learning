# 一、字符串的定义
# 1、单引号定义
# 2、双引号定义
# 3、三引号定义多行字符串


# 二、字符串的索引与切片
# 1、索引
words = '精诚所至金石为开'
# <1、正向索引，与C语言一致
char_one = words[0]
print(char_one)
char_two = words[1]
print(char_two)
# <2、逆向索引，从右至左由-1开始递减
CHAR_ONE = words[-8]
print(CHAR_ONE)
CHAR_TWO = words[-7]
print(CHAR_TWO)

# 2、切片
#索引获取单个字符，切片可以从字符串中截取字串
#格式：字符串[起始索引:结束索引:步长]
#步长：表示每隔指定数量的字符截取一次字符串，取值可以是正、负整数，正表示从左到右取，负则相反
print(words[:5])
print(words[5:])
print(words[4:6])
print(words[::2])
print(words[-4:-2])
print(words[-4:6])
print(words[::-1])   #逆序输出字符串

#实例、制作高铁名片
model = input("请输入型号：")
nicknamae = input("请输入外号：")
power_source = input("请输入动力来源：")
speed = input("请输入速度：")
use_time = input("请输入投用时间：")
print("复兴号电力动车组")
print("===============================")
print(f"型号：{model}")
print(f"外号：{nicknamae}")
print(f"动力来源：{power_source}")
print(f"速度：{speed}")
print(f"投用时间：{use_time}")
print("===============================")
print("2022年12月入选“2022全球十大工程成就”")


#三