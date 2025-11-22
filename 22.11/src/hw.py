import random

def task1():
    a = []

    for i in range(5):
        for j in range(5):
            if j == 0:
                a.append([])
            a[i].append(random.randint(0, 100))
    
    print("Початковий масив:")
    for row in a:
        print(row)

    for i in range(5):
        for j in range(i + 1, 5):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    print("\nПісля перестановки:")
    for row in a:
        print(row)


def task2():
    a = []

    for i in range(5):
        for j in range(5):
            if j == 0:
                a.append([])
            a[i].append(random.randint(0, 100))

    print("\nПочатковий масив:")
    for row in a:
        print(row)

    n = 5
    for i in range(n):
        a[i][i], a[i][n - 1 - i] = a[i][n - 1 - i], a[i][i]

    print("\nПісля перестановки головної та бічної діагоналей:")
    for row in a:
        print(row)


def task3():
    a = [[random.randint(-100, 100) for _ in range(5)] for _ in range(5)]

    print("Масив:")
    for row in a:
        print(row)

    flat = []
    for i in range(5):
        for j in range(5):
            flat.append(a[i][j])


    min_value = flat[0]
    max_value = flat[0]
    min_index = 0
    max_index = 0

    for i in range(25):
        if flat[i] < min_value:
            min_value = flat[i]
            min_index = i
        if flat[i] > max_value:
            max_value = flat[i]
            max_index = i

    left = min(min_index, max_index)
    right = max(min_index, max_index)

    total = 0
    for i in range(left + 1, right):
        total += flat[i]

    print(f"\nМінімальний елемент ({min_value}) на позиції {min_index}")
    print(f"Максимальний елемент ({max_value}) на позиції {max_index}")
    print(f"Сума між ними = {total}")

    return total

task1()
task2()
task3()