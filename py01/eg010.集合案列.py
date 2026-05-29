#选择足球的学生
football_set = {"王林","曾牛","徐立国","遁天","天运子","韩立","历飞雨","乌丑","紫灵"}
#选择篮球的学生
basketball_set = {"张铁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","历飞雨","云露"}
#选择法语的学生
french_set = {"许木","王卓","十三","虎咆","姜老道","天运子","红碟","历飞雨","韩立","曾牛"}
#选择艺术的学生
art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

#1、选出同时选修法语和艺术的学生
#方式一：库函数
# f_and_a = art_set.intersection(french_set)
# print("同时选修法语和足球的学生：",f_and_a)
#方法二：& --> 求交集
f_and_a2 = art_set & french_set
print("同时选修法语和足球的学生：",f_and_a2)

#2、找出同时选择四门课的学生
all_set = football_set & basketball_set & art_set & french_set
print("同时选修四门课的学生：",all_set)

#3、找出选修足球但没选篮球的学生

#方法一：库函数
# f_no_b = football_set.difference(basketball_set)
# print("选修足球但没选篮球的学生:",f_no_b)

#方法二：- ——> 差集
# f_no_b2 = football_set- basketball_set
# print("选修足球但没选篮球的学生:",f_no_b2)

#方法三：集合推导式
f_no_b3 = {stu for stu in football_set if stu not in basketball_set}
print("选修足球但没选篮球的学生:",f_no_b3)

#4、统计每一个学生选修的课程数量

#先获取所有学生名单（求并集）

#方法一：库函数
ALL_set1 = football_set.union(basketball_set).union(art_set).union(french_set)
ALL_set2 = football_set.union(basketball_set,art_set,french_set)
# print(ALL_set1)
# print(ALL_set2)
#方法二：| ——> 并集
ALL_set3 = football_set | basketball_set | art_set | french_set
# print(ALL_set3)
#方法三：解包
ALL_set4 = {*football_set, *basketball_set, *art_set, *french_set}
# print(ALL_set4)

#统计每个学生选课数量
ALL_list = [*football_set, *basketball_set, *art_set, *french_set]

for stu in ALL_set4:
    print(f"{stu}选修了{ALL_list.count(stu)}课程")