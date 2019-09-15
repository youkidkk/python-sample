# 宣言
dic = {"k1": "hoge", "k2": "fuga"}
print(dic)
# -> {'k1': 'hoge', 'k2': 'fuga'}

# 要素の参照
print(dic["k1"])
# -> hoge

# 要素の追加
dic["k3"] = "piyo"
print(dic)
# -> {'k1': 'hoge', 'k2': 'fuga', 'k3': 'piyo'}

# in（キーの存在）
print("k1" in dic)
# -> True
print("hoge" in dic)
# -> False

# キーのリスト
print(list(dic.keys()))
# -> ['k1', 'k2', 'k3']

# for
for k, v in dic.items():
    print("{0} : {1}".format(k, v))
# -> k1 : hoge k2 : fuga k3 : piyo

# dict関数による作成
dic2 = dict([("kk1", "hogehoge"), ("kk2", "fugafuga")])
print(dic2)
# -> {'kk1': 'hogehoge', 'kk2': 'fugafuga'}
