from abc import ABCMeta, abstractmethod


# 抽象クラス
# metaclass=ABCMeta を指定する
class AbstractClass(metaclass=ABCMeta):

    # 抽象メソッド
    # @abstractmethod を指定する
    @abstractmethod
    def method(self):
        pass


class ImplClass(AbstractClass):
    def method(self):
        print("Impl Class - method")


c = ImplClass()
c.method()
