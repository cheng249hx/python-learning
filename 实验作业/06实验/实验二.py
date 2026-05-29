print("实验二：")
def info(name,age,city):
    print(name,f"{age}岁",f"来自{city}")
def info_default(name,age=18,city="北京"):
    print(name,f"{age}岁",f"来自{city}")

def student(name,grade,score):
    print(name,f"{grade}年级",f"{score}分")
#位置参数传递
info("张三",20,"北京")
#不覆盖
info_default("李四")
#覆盖
info_default("王五",25,"上海")
#关键字传递
student(name="小明",grade=2,score=95)