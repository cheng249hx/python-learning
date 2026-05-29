s = "Hello-Python-Hello-world"

#1、find()查找指定子串第一次出现的位置
pos = s.find("P")
print(pos)

#2、count()统计子串出现的次数
con = s.count("Hello")
print(con)

#3、upper()转圜为大写
str1 = s.upper()
print(str1)

#4、lower()转换为小写
str2 = s.lower()
print(str2)

#5、split()切割字符串
list_str = s.split("-")
print(list_str)

#6、replace()将指定子串替换为新内容
str3 = s.replace("Hello", "AAAAA")
print(str3)