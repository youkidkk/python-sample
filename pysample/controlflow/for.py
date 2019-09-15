# 基本（シーケンス型による反復）
list = ["abc", "def", "ghi"]
for item in list:
    print(item)

# range関数による繰り返し
for i in range(10):  # -> 0 - 9
    print(i)
for i in range(5, 10):  # -> 5 - 9
    print(i)

# continue、break
for i in range(10):
    if i % 2 == 0:
        continue
    if i > 8:
        break
    print(i)
# -> 1 3 5 7

# else（ループ終了時の処理）
for i in range(5):
    print(i)
else:
    print("End!")
# -> 0 1 2 3 5 End!

# break時は実行されない
for i in range(5):
    if i > 3:
        break
    print(i)
else:
    print("End!")
# -> 0 1 2 3
