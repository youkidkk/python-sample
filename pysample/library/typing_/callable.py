from typing import Callable


def method(callable: Callable[[int], str], i: int):
    # Callable の使用例
    # 引数がintで戻り値がstrのメソッドを定義
    return callable(i)


def p_method(i: int) -> str:
    return str(i)


print(method(p_method, 123))
