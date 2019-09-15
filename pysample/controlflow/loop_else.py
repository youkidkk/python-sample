for i in range(3):
    print(i)
# else句はループの後に実行される
else:
    print("End.")

for i in range(3):
    print(i)
    if i == 2:
        break
# breakされた場合は実行されない
else:
    print("End.")
