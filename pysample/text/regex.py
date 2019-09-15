import re

text = "Hello Python!!!"
pattern = "[A-Z][a-z]+"

# 先頭から最初にマッチした部分を取得
result = re.match(pattern, text)
if result:
    # マッチ部分の位置を取得
    print(result.span())  # -> (0, 5)
    # マッチ部分の文字列を取得
    print(result.group())  # -> Hello

# マッチした部分のリストを取得
list = re.findall(pattern, text)
if list:
    print(", ".join(list))  # -> Hello, Python

# 置換
print(re.sub(pattern, "<Word>", text))  # -> <Word> <Word>!!!

# 後方参照
pattern = "Hello ([A-Z][a-z]+)!!!"
print(re.sub(pattern, r"Match part: \1", text))  # -> Match part: Python
