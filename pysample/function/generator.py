# 指定文字列の文字を先頭から順に返却するジェネレータ
def gen_sample(text):
    for i in range(len(text)):
        # return の代わりに yield で値を返す
        yield text[i]


for c in gen_sample("あいうえお"):
    print(c)
    # あ→い→う→え→お
