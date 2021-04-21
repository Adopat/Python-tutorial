# 循环有三种 for循环，while 循环 和嵌套循环
items = ["Abby","Brenda","Cindy","Diddy"]
for item in items:
    print(item)
# for 循环可以重复N次
for i in range(1,10):
    print(i)
# while 循环，如果不确定循环多少次，使用while 循环
print("=====while=====")
correctNumber = 5
guess = 0
while guess !=correctNumber:
    guess = int(input("Guess the number:"))
    if guess !=correctNumber:
        print('False guess')
print('You guessed the correct number')
# 嵌套循环
print("=====嵌套循环=====")
for x in range(1,10):
    for y in range(1,10):
        print("(" + str(x) + "," + str(y) + ")")