#用小括号定义元组
#元组内的值不可修改
a = (21, 32, 423, 42, 7, 12,32)
print(a)

#索引

#切片

#count()统计指定元素出现的次数
con1 = a.count(32)
print(con1)

#index()查询指定元素的索引（第一次出现位置的索引）
pos = a.index(32)
print(pos)

#组包

#解包（）
#基础解包（变量元素与容器元素个数一至）
A,B,C,D,E,F,G = a
print(A,B,C,D,E,F,G)
#扩展解包
first,*other,last = a
print(first)
print(other)
print(last)