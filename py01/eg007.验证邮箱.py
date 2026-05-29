#用户输入一个邮箱，验证邮箱格式是否正确（至少包含一个'@'和一个'.'）

str1 = input("请输入邮箱：")

con1 = str1.count("@")
con2 = str1.count(".")

if con1 >= 1 and con2 >= 1:
    print("邮箱输入正确！")
else:
    print("邮箱输入错误！")