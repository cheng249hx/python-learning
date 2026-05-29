list_one = [12,423,36,12,35,64,34,36]
list_two = [421,423,536,42,456,77,35,2423]

# 1、合并
# for num in list_two:
#     list_one.append(num)
list_one += list_two

print("原始列表为：",list_one)

#2、去重
list_tmp = []

for num  in list_one:
    if num in list_tmp:
        print(f"去除重复元素{num}")
        continue
    else:
        list_tmp.append(num)

print("去重后列表为：",list_tmp)