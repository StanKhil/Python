import time

# task 1
def task1(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield i

print("task 1:")
for num in task1(1, 20):
    print(num, end=" ")
print("\n")

# task 2
def task2(lst, start, end):
    for x in lst:
        if x < start or x > end:
            yield x

print("task 2:")
lst = [1, 5, 10, 15, 20, 25]
for num in task2(lst, 7, 18):
    print(num, end=" ")
print("\n")

# task 3
def task3(symbol, function_to_call):
    function_to_call(symbol)

def horizontal_line(symbol):
    print(symbol * 10)

def vertical_line(symbol):
    for _ in range(5):
        print(symbol)

print("task 3:")
task3("*", horizontal_line)
task3("#", vertical_line)
print("\n")

# task 4
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд")
        return result
    return wrapper

@timer
def task4():
    return [i for i in range(0, 1001) if i % 2 == 0]

print("task 4:")
evens = task4()
print(evens)
print("\n")

# task 5
@timer
def task5(start, end):
    return [i for i in range(start, end + 1) if i % 2 == 0]

print("task 5:")
evens_range = task5(10, 50)
print(evens_range)
