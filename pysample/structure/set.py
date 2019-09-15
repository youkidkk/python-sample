# 宣言
set1 = {"hoge", "fuga", "piyo", "hoge"}
print(set1)
# -> {'hoge', 'fuga', 'piyo'}
# ※ 重複は削除される

# in
print("hoge" in set1)
# -> True
print("fugafuga" in set1)
# -> False

# 演算
set2 = {"hoge", "piyo", "piyopiyo"}
print(set1 & set2)
# -> {'hoge', 'piyo'}
print(set1 | set2)
# -> {'fuga', 'piyo', 'piyopiyo', 'hoge'}
print(set1 - set2)
# -> {'fuga'}
print(set1 ^ set2)
# -> {'fuga', 'piyopiyo'}
