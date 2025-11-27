
def decorator(func, pre, post):
    def wrapper():
        print(pre)
        func()
        print(post)

    return wrapper

 
 
@decorator("######################", "-------------------------")
def hello():
    print("Hello")
 
hello()
 