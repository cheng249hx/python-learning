"""
定一个函数，用于根据传入的一批商品信（商品名称、价格、数量）、优惠券、积分、运费计算订单的总金额，具体规则如下
    ·优惠券需要商品总金额满5000才可以使用，且优惠券金额不能超过商品总金额
    ·积分需要商品总金额满5000才可以使用，100个积分抵扣一元(且优积分金额不能超过商品总金额，积分只能整百抵扣)
"""

def fun(*goods: tuple[str,float,int], you_hui: float=0.0, score: int=0,yun_fei: float=0.0)->float:
    """
    :param goods: 商品信息 ——> (商品名称，价格，数量)
    :param you_hui: 优惠券金额
    :param score: 积分数量
    :param yun_fei: 运费信息
    :return: 订单总金额
    """
    #列表推导式获取每种商品的总价
    good_price = [good[1] * good[2] for good in goods]
    all_price = sum(good_price)

    #核减优惠券
    if all_price >= 5000 and you_hui <=all_price:
        all_price -= you_hui

    #抵扣积分
    if all_price >= 5000 and score // 100 <= all_price:
        all_price -=score // 100

    #加上运费
    all_price += yun_fei

    return all_price



print(fun(("手机",3999,1),("鼠标",188,2),("键盘",388,1), you_hui=10, score=4000, yun_fei=9.9))
print(fun(("手机",6999,1),("鼠标",188,2),("键盘",388,1), you_hui=10, score=4000, yun_fei=9.9))

#运费、积分、优惠券设置了默认值，如果没有需要可以不传参
print(fun(("手机",3999,1),("鼠标",188,2),("键盘",388,1)))

a = (("手机",3999,1),("鼠标",188,2),("键盘",388,1))
#此时需要进行解包，保证实参与形参类型一致
print(fun(*a))