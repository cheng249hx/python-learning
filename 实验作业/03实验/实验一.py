score = float(input("请输入分数: "))
if 90 <= score <= 100:
    print("评级: A")
elif 80 <= score < 90:
    print("评级: B")
elif 70 <= score < 80:
    print("评级: C")
elif 60 <= score < 70:
    print("评级: D")
else:
    print("分数不在评级范围内")