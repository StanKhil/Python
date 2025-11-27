# Task 1
def task1(start, end):
    a, b = 0, 1
    while a <= end:
        if a >= start:
            yield a
        a, b = b, a + b

print("Task 1:")
for num in task1(5, 50):
    print(num, end=" ")
print("\n")

# Task 2
def task2(lst1, lst2):
    max_len = max(len(lst1), len(lst2))
    for i in range(max_len):
        val1 = lst1[i] if i < len(lst1) else 0
        val2 = lst2[i] if i < len(lst2) else 0
        yield val1 + val2

print("Task 2:")
list1 = [1, 3, 4, 2]
list2 = [8, 3, 5, 9]
for s in task2(list1, list2):
    print(s, end=" ")
print("\n")

# Task 3
def task3(list_to_work, function_to_call):
    lst = []
    for x in list_to_work:
        lst.append(function_to_call(x))
    return lst

def square(x):
    return x * x

def cube(x):
    return x * x * x

print("Task 3:")
numbers = [1, 2, 3, 4]
print("Квадрат:", task3(numbers, square))
print("Куб:", task3(numbers, cube))
print("\n")

# Task 4
def task4(org_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Фінансова звітність для {org_name}:")
            result = func(*args, **kwargs)
            print()
            return result
        return wrapper
    return decorator

@task4("Податкова")
def tax_report(data):
    print("Дані:", data)

@task4("Статистичне бюро")
def stats_report(data):
    print("Дані:", data)

print("Task 4:")
tax_report({"дохід": 10000, "витрати": 5000})
stats_report([10, 20, 30, 40])
