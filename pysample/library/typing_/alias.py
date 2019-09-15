from typing import Tuple

# 型エイリアスの定義
Name = Tuple[str, str]


def introduce_oneself(name: Name):
    # 定義したエイリアスの利用
    print("I am " + name[0] + ", " + name[0] + " " + name[1] + ".")


introduce_oneself(("Taro", "Yamada"))
