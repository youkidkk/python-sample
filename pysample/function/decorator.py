# デコレータの宣言
def deco(func):
    def wrapper(*args, **kwargs):
        print("Args : {0}".format(args))
        print("Keyword Args : {0}".format(kwargs))
        func(*args, **kwargs)

    return wrapper


@deco
def test(x, y, z="hoge"):
    print("test method. x:{0}, y:{1}, z:{2}".format(x, y, z))


test(1, 2, z="fuga")


# 引数ありのデコレータ
def arg_deco(arg):
    def _deco(func):
        def _decorated(*args, **kwargs):
            print(arg)
            func(*args, **kwargs)

        return _decorated

    return _deco


@arg_deco("hoge")
def test2(x, y, z="hoge"):
    print("test method. x:{0}, y:{1}, z:{2}".format(x, y, z))


test2(1, 2, z="fuga")
