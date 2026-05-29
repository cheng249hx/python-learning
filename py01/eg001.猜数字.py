import random

num_set = random.randint(1,100)

while True:
    a = int(input("请输入你猜的数字："))
    if a > num_set:
        print("猜大了")
    elif a < num_set:
        print("猜小了")
    else :
        print("恭喜你猜对了! 666!")
        break

print(f"随机生成的数字是{num_set}")
