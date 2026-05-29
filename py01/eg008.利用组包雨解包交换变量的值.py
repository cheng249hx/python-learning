a = 20
b = 10

a,b = a,b
print(a)
print(b)
print(a,b)
#原理
t = b,a #组包
a,b = t #解包
#合并后即为上式
# a,b = (b,a) 更好理解

#交换三个数的值同理
a = 1
b = 2
c = 3
a,b,c = c,a,b
print(a,b,c)