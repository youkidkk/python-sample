# 宣言
list = [1, 2, 3, 4, 5]
print(list)
# -> [1, 2, 3, 4, 5]

# 要素数取得
print(len(list))
# -> 5

# 要素の参照
# 先頭から
print(list[1])
# -> 2
# 末尾から
print(list[-1])
# -> 5

# スライス
# 先頭からN番目以降
print(list[2:])
# -> [3, 4, 5]
# 先頭からN番目まで
print(list[:2])
# -> [1, 2]
# 末尾からN番目まで
print(list[-2:])
# -> [4, 5]
# 末尾からN番目以降
print(list[:-2])
# -> [1, 2, 3]

# 要素の追加
list.append(6)
list.append(7)
list.append(8)
print(list)
# -> [1, 2, 3, 4, 5, 6, 7, 8]

# インデックス指定で要素を削除
del list[5]
print(list)
# -> [1, 2, 3, 4, 5, 7, 8]
# インデックス指定で要素を削除と値の取得
p = list.pop(5)
print(p, list)
# -> 7 [1, 2, 3, 4, 5, 8]

# 要素の挿入
list.insert(2, 8)
print(list)
# -> [1, 2, 8, 3, 4, 5, 8]

# 値を指定した要素の削除
# ※ 先頭から検索して最初の該当値のみ削除する
# ※ 該当値がない場合はエラーとなる
list.remove(8)
print(list)
# -> [1, 2, 3, 4, 5, 8]

# リスト内包表記
squares = [n ** 2 for n in range(10)]
print(squares)
# -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# リスト同士の結合（extend）
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
# -> [1, 2, 3, 4, 5, 6]
