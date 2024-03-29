import numpy as np

# NumPy配列の生成
nparr = np.array([1, 2, 3])
print(nparr)  # -> [1 2 3]

# 要素の参照
print(nparr[0])  # -> 1

print(
    "type: {}, shape: {}, size: {}".format(
        nparr.dtype,  # データタイプ -> int32
        nparr.shape,  # 配列の構造 -> (3,)
        nparr.size,  # サイズ -> 3
    )
)

# 要素の追加
nparr = np.append(nparr, [4, 5, 6])
print(nparr)  # -> [1 2 3 4 5 6]

# 次元を変換
print(nparr.reshape(2, -1))  # -> [[1 2 3] [4 5 6]]

# 加算、減算、乗算
print(nparr + 1)  # -> [2 3 4 5 6 7]
print(nparr - 1)  # -> [0 1 2 3 4 5]
print(nparr * 2)  # -> [ 2  4  6  8 10 12]

# 最小/最大値、増分を指定して配列を生成
rng5 = np.arange(0, 5.0, 0.5)
print(rng5)  # -> [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]
