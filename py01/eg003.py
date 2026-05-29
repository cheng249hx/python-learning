#将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中最大值和最小值和平均值

a_list = []

for i in range(1,11):
    a = int(input(f"请输入第{i}个整数"))
    a_list.append(a)

print("排序前的列表", a_list)

print(f"最大值为{max(a_list)}")
print(f"最小值为{min(a_list)}")
print(f"平均值为{sum(a_list) / len(a_list)}")

a_list.sort()

print("排序后的列表", a_list)