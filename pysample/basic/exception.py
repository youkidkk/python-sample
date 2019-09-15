# 基本
try:
    i = int("hoge")
except ValueError:
    print("ValueError!")

# as（例外オブジェクトの取得）
try:
    i = int("hoge")
except ValueError as err:
    print(err)

# raise（例外の送出）
try:
    raise ValueError("fuga")
except ValueError as err:
    print(err)

# finally
try:
    i = int("hoge")
except ValueError as err:
    print(err)
finally:
    print("Finish!")


# ユーザー定義例外
class NewException(Exception):
    pass


try:
    raise NewException
except NewException:
    print("Error!")
