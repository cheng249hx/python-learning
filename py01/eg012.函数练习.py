#定义一个函数求一组数据的平均值，在最大值，最小值
def mma(data_list):
    return min(data_list), max(data_list), sum(data_list)/len(data_list)

a = [13, 14, 15, 16]
MIN,MAX,AVE = mma(a)
print(MIN, MAX, AVE)