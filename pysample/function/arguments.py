def func(arg1, *args):
    print("arg1: " + arg1 + " args: " + ",".join(args))


func("1", "2", "3")
# -> arg1: 1 args: 2,3

func("1")
# -> arg1: 1 args:
