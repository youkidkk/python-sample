# 宣言
tuple = 123, 456, "abc"
# 以下でも可
# tuple = (123, 456, "abc")
print(tuple)
# -> (123, 456, 'abc')

# Immutableなため、再代入は不可
# tuple[0] = 789
# -> Error

# for文
for e in tuple:
    print(e)
# -> 123 456 abc

# 要素の取得
print(tuple[1])
# -> 456

# ネストしたタプル
nested = "xxx", tuple
print(nested)
# -> ('xxx', (123, 456, 'abc'))

# ネストした要素の取得
print(nested[1][2])
# -> abc
