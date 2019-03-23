import random
secret=random.randint(1,10)
print("=======This is Shuguberu=======")
temp=input("输入数字")
guess=int(temp)
while guess!=secret:
    temp=input("wrong,once again:")
    guess=int(temp)
    if guess==secret:
        print("right")
    else:
        if guess>secret:
            print("大了")
        else:
            print("小了")
print("over")
