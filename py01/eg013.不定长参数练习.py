#定义一个函数求一组数据的平均值，在最大值，最小值
def mma(*data,**kwargs):
    min_data = min(data)
    max_data = max(data)
    ave_data = sum(data)/len(data)

    if kwargs.get("round") is not None:
        ave_data = round(ave_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值{min_data}\n最大值{max_data}\n平均值{ave_data}")

    return min_data,max_data,ave_data

print(mma(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
mma(143,535,645,67,658,58,54343,round = 2, print = True)