# スーパークラス
class Parent:
    def func1(self):
        print("func1!")


# 継承したクラス


class Child(Parent):
    def func2(self):
        super().func1()  # スーパークラスのメソッド呼び出し
        print("func2!")


child = Child()

# スーパークラスのメソッド呼び出し
child.func1()

# 継承したクラスのメソッドの呼び出し
child.func2()
