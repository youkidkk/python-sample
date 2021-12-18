"""クラスの基本"""


class SampleClass:
    """Sample Class"""

    class_var = "Class variable"
    """クラス変数"""

    @classmethod
    def class_method(cls, arg):
        """クラスメソッド
        ・ @classmethod を付与する
        ・ 第一引数に自身のクラス（"cls"）を受け取る
        """
        print("Class method.")
        print("  Class var : {0}, Arg : {1}".format(cls.class_var, arg))

    @staticmethod
    def static_method(arg):
        """スタティックメソッド
        ・ @staticmethod を付与する
        ・ クラス変数は参照できない
        """
        print("Static method.")
        print("  Arg : {0}".format(arg))

    def __init__(self, ins_var1, ins_var2):
        """コンストラクタ
        ・ メソッド名を"__init__"とする
        ・ 第一引数に自身のインスタンス（"self"）を受け取る
        """
        self.ins_var1 = ins_var1
        self.ins_var2 = ins_var2

    def instance_method(self, arg):
        """インスタンスメソッド
        ・ 第一引数に自身のインスタンス（"self"）を受け取る
        """
        print("Instance method : ")
        print(
            "  Var1 : {0}, Var2 : {1}, Arg : {2}".format(
                self.ins_var1, self.ins_var2, arg
            )
        )

    # 文字列化メソッド
    def __str__(self):
        """文字列化メソッド
        ・ メソッド名を"__str__"とする
        ・ 第一引数に自身のインスタンス（"self"）を受け取る
        """
        return "Var1 : {0}, Var2 : {1}".format(self.ins_var1, self.ins_var2)


# クラス変数の参照
print(SampleClass.class_var)

# クラスメソッドの呼び出し
SampleClass.class_method("hoge")

# スタティックメソッドの呼び出し
SampleClass.static_method("hoge")

# インスタンスの生成
sample = SampleClass("hoge", "fuga")

# インスタンスメソッドの呼び出し
sample.instance_method("piyo")

# 文字列化
print(sample)
