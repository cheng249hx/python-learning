#完成如下列表操作:
data_list = ["Python","C++","Java","PHP","JavaScript","HTLM5","CSS"]

#按照列表的元素字符个数进行排序
data_list.sort(key=lambda item: len(item))
print("按照列表的元素字符个数进行升序",data_list)
data_list.sort(key=lambda item: len(item),reverse=True)
print("按照列表的元素字符个数进行降序",data_list)

#按照列表的元素字符'S'个数进行排序
data_list.sort(key=lambda item: item.count("S"))
print("按照列表的元素字符'S'个数进行升序",data_list)
data_list.sort(key=lambda item: item.count("S"),reverse=True)
print("按照列表的元素字符'S'个数进行降序",data_list)