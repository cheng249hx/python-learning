a_list = []

for i in range(1,21):
    t = i ** 2
    a_list.append(t)

print(a_list)

#提取列表中的偶数，计算其平方再生成一个新的列表

list_tmp = []

for num in a_list:
    if num % 2 == 0:
        list_tmp.append(num ** 2)

print(list_tmp)