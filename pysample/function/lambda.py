def func(filter):
    for i in range(10):
        if filter(i):  # 引数のラムダ式の利用
            print(i)


# ラムダ式を渡す
func(lambda x: x % 3 == 1)
