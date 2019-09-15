from unittest.mock import patch


def method():
    return "hoge"


# コンテキストマネージャを使用したパッチ
with patch("__main__.method", return_value="fuga"):
    print(method())
    # -> fuga


@patch("__main__.method")
# デコレータを使用したパッチ
def test(mock):
    mock.return_value = "piyo"
    print(method())


test()
# -> piyo
