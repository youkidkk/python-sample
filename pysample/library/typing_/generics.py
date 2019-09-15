from typing import TypeVar

# ジェネリクスの定義
T = TypeVar("T")


def method_t(arg: T):
    # ジェネリクスの使用
    print(arg)


method_t(1)
method_t("abc")

# 有効な型を指定してジェネリクスを定義
U = TypeVar("U", str, int)


def method_u(arg: U):
    # ジェネリクスの使用
    print(arg)


method_u("abc")
method_u(123)
# 以下は型が一致しないためエラー
# method_u(1.5)
