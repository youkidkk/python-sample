s = "String!!!"

print(s)

# 文字列をx回繰り返す
print(s * 5)  # -> String!!!String!!!String!!!String!!!String!!!

# x番目の文字列を返す（0オリジン）
print(s[3])  # -> i

# x番目からy-1番目の文字列を返す（0オリジン）
print(s[1:4])  # -> tri

# 文字列長を返す
print(len(s))  # -> 9

# 文字列の前に r を付与でエスケープシーケンスを無効化
s = r"\r\n\t"
print(s)  # -> \r\n\t

# 区切り文字を指定して文字列リストを結合
list = ["abc", "def", "ghi"]
print(", ".join(list))  # -> abc, def, hgi
