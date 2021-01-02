def func(**keywords):
    for k, v in keywords.items():
        print("{}:{}".format(k, v))


func(a=1, b=2, c=3)
# ->
# a:1
# b:2
# c:3
