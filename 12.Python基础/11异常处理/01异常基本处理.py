person = {"username":"zhiliao","age":18}

# try:
#     username = person['username1']
#     print(username)
# except KeyError:
#     print("没有这个key")


try:
    a = 1
    b = 0
    c = a/b

    print(c)
# except ZeroDivisionError:
except Exception as e:
    print(e)
    print('走到except中了')
else:
    print('走到else中了')
finally:
    print('走到finally中了')

# 异常：
# 1. 为什么需要异常处理：异常如果出现了，可能会导致程序直接崩溃退出，所以需要对那些可能会出现异常的地方用try进行捕获。
# 2. 在except中，可以直接写明异常的名字，比如ZeroDivisionError，这样捕获会更加精准，但是如果try中出现了其他的异常就不能被捕获了。
# 3. 如果想要捕获所有异常，那么就可以使用Exception，就可以把try中出现的所有异常都捕获到。