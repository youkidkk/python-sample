def func_if(num):
    # if
    if num < 0:
        print("{0} is less than 0.".format(num))
    elif num < 2:
        print("{0} is less than 2.".format(num))
    else:
        print("{0} isn't less than 2.".format(num))


func_if(-1)
func_if(1)
func_if(2)


def func_ternary_op(num):
    # 三項演算子
    str = "Even" if num % 2 == 0 else "Odd"
    print("{0} is {1} number.".format(num, str))


func_ternary_op(1)
func_ternary_op(2)
