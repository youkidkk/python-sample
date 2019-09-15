class MyClass:

    # Publicメソッド（）
    def public(self):
        print("Public!!!")

    # Privateメソッド（メソッド名先頭を"__"とする）
    def __private(self):
        print("Private!!!")


myClass = MyClass()
myClass.public()

# 以下はプライベートメソッド呼び出しとなるためエラー
# myClass.__private()

# 無理やりプライベートメソッドを呼び出す方法
# myClass._MyClass__private()
