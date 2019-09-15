from unittest.mock import MagicMock


# モックオブジェクトの設定
method = MagicMock()

# 戻り値を指定
method.return_value = 10
print(method(1, 2))
# -> 10
print(method(3, 4))
# -> 10
print(method(5, 6))
# -> 10

# 呼び出されたかどうか確認
method.assert_called()

# 指定した引数での呼び出しがあったか確認
method.assert_any_call(3, 4)

# 直前に指定した引数での呼び出しがあったか確認
method.assert_called_with(5, 6)

# 呼び出し引数の取得
print(method.call_args_list)
# -> [call(1, 2), call(3, 4), call(5, 6)]
print(method.call_args_list[1])
# -> call(3, 4)

# 直前の呼び出し引数の取得
print(method.call_args)
# -> call(5, 6)

# 呼び出し回数の取得
print(method.call_count)
# -> 2

# 呼び出し毎の戻り値を指定
method.side_effect = [1, 2, 3]
print(method(), method(), method())
# -> 1 2 3
