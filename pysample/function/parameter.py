def parameter(x, y=1, z=2):
    print(x, y, z)


# 通常の呼び出し
parameter(2, 3, 4)
# -> 2 3 4

# 引数の省略して呼び出し
parameter(3, 4)
# -> 3 4 2
parameter(4)
# -> 4 1 2

# キーワードで指定して呼び出し
parameter(5, z=6)
# -> 5 1 6

# 引数リストのアンパック
args = [3, 4, 5]
parameter(*args)
# 3 4 5
