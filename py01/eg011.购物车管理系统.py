dict1 = {}

while True:
    print("欢迎使用购物车管理系统！")
    print()
    print("#########################")
    print("#      1.添加购物车       #")
    print("#      2.删除购物车       #")
    print("#      3.修改购物车       #")
    print("#      4.查询购物车       #")
    print("#      5.退出购物车       #")
    print("#########################")
    op = int(input("请选择对应功能序号："))
    if op == 1:
        name = input("请输入商品名称：")
        price = int(input("请输入商品价格："))
        con = int(input("请输入商品数量："))
        dict1[name] = [price,con]
        print("添加成功！")
    elif op == 2:
        name = input("请输入要删除的商品名称：")

        del dict1[name]
        print("删除成功！")
    elif op == 3:
        name = input("请输入要修改的商品名称：")
        price = int(input("请输入商品价格："))
        con = int(input("请输入商品数量："))
        dict1[name] = [price,con]
        print("修改成功！")
    elif op == 4:
        for name in dict1.keys():
            price,con = dict1[name]
            print(f"{name}:价格{price}、数量{con}")
            print("查询成功！")
    elif op == 5:
        break
