class FibonacciIterator:
    def __init__(self, max):
        self._max = max
        self._n1 = 0
        self._n2 = 1

    def __iter__(self):
        # __iter__メソッド -> イテレータの取得
        return self

    def __next__(self):
        # __next__メソッド -> 繰り返し毎の値を返却
        result = self._n1 + self._n2
        if result > self._max:
            # StopIteration例外 -> 繰り返しの終了
            raise StopIteration
        self._n1 = self._n2
        self._n2 = result
        return result


fibo_iter = FibonacciIterator(1000)
for n in fibo_iter:
    print(n)
