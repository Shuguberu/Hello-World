print("=======This is Shuguberu=======")
temp=input("输入数字")
guess=int(temp)
while guess!=8:
    temp=input("wrong,once again:")
    guess=int(temp)
    if guess==8:
        print("right")
    else:
        if guess>8:
            print("大了")
        else:
            print("小了")
print("over")
