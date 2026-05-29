students = (
("S001","王林",85,92,78),
("S002","李慕婉",92,88,95),
("S003","十三",78,85,82),
("S004","曾牛",88,79,91),
("S005","周佚",95,96,89),
("S006","王卓",76,82,77),
("S007","红蝶",89,91,94),
("S008","许立国",75,69,82),
("S009","许木",86,89,98),
("S010","遁天",66,59,72),
)

#1、计算每个学生总分、平均分然后输出
#打印表头
print("学号\t\t 姓名\t 语文\t 数学\t 英语\t 总分\t 平均分")
#方法一
# for student in students:
#     stuID,name,*score = student #解包将所有成绩放入一个列表中
#     ave = sum(score)/len(score)
#     print(f"{stuID} \t {name} \t {score[0]} \t {score[1]} \t {score[2]} \t {sum(score)} \t {ave:.1f}")

#方法二
for stuID,name,Chinese,Math,English in students: #解包操作
    sum_score = Chinese +  Math +  English
    ave = (Chinese +  Math +  English)/3
    print(f"{stuID} \t {name} \t {Chinese} \t {Math} \t {English} \t {sum_score} \t {ave:.1f}")

#2、计算各科平均分，最高分，最低分
#或许各科成绩列表
Chinese_score = [s[2] for s in students]
Math_score = [s[3] for s in students]
English_score = [s[4] for s in students]

print(f"语文:最高分{max(Chinese_score)}\t最低分{min(Chinese_score)}\t平均分{sum(Chinese_score)/len(Chinese_score)}")
print(f"数学:最高分{max(Math_score)}\t最低分{min(Math_score)}\t平均分{sum(Math_score)/len(Math_score)}")
print(f"英语:最高分{max(English_score)}\t最低分{min(English_score)}\t平均分{sum(English_score)/len(English_score)}")

#3、查找成绩优秀的学生（平均分大于90）并输出
print("优秀学生(平均分 > 90)名单如下")
for student in students:
    stuID,name,*score = student #解包将所有成绩放入一个列表中
    ave = sum(score)/len(score)
    if ave > 90:
        print(f"学号：{stuID}\t姓名：{name}\t平均分：{ave:.1f}")
