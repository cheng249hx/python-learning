print("实验一：")

def change(tem: float, ch: str) -> list[float|str]:
    if  ch == "C":
        return [tem + 273.15, "K"]
    elif ch == "K":
        return [tem - 273.15, "C"]
    else:
        print("输入有误！")
        return []

a = input("请输入温度和单位（摄氏度C、开氏度K）：")
b = float(a[:-1])
if change(b,a[-1]):
    tem, ch = change(b, a[-1])
    if ch == "C":
        print(f"转换后的温度为{tem:.2f}{ch}")
    elif ch == "K":
        print(f"转换后的温度为{tem:.2f}{ch}")