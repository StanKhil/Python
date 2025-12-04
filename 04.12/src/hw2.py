import pickle
import os

# Завдання 1

def task1():
    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()
    text = text.replace("Python", "Java")
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(text)


# Завдання 2

def task2():
    with open("data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("char_count.txt", "w", encoding="utf-8") as f:
        i = 1
        for line in lines:
            f.write(f"Рядок {i}: {len(line)} символів\n")

# Завдання 3

def task3():
    with open("old_version.txt", "r", encoding="utf-8") as f:
        old = set(f.readlines())
    with open("new_version.txt", "r", encoding="utf-8") as f:
        new = set(f.readlines())
    diff = (old - new) | (new - old)
    with open("differences.txt", "w", encoding="utf-8") as f:
        for line in diff:
            f.write(line)


# Завдання 4

def task4():
    with open("words.txt", "r", encoding="utf-8") as f:
        bad = [w.strip() for w in f.readlines()]
    with open("source.txt", "r", encoding="utf-8") as f:
        text = f.read()
    for w in bad:
        text = text.replace(w, "***")
    with open("censored.txt", "w", encoding="utf-8") as f:
        f.write(text)


# Завдання 5

orders_file = "orders.bin"

def load_orders():
    if not os.path.exists(orders_file):
        return {}
    try:
        with open(orders_file, "rb") as f:
            return pickle.load(f)
    except:
        return {}

def save_orders(orders):
    with open(orders_file, "wb") as f:
        pickle.dump(orders, f)

def task5():
    while True:
        print("\n1 Додати")
        print("2 Переглянути")
        print("3 Пошук")
        print("4 Оновити")
        print("5 Видалити")
        print("6 Вихід")
        choice = input("> ")

        orders = load_orders()

        if choice == "1":
            num = input("Номер: ")
            item = input("Товар: ")
            qty = int(input("Кількість: "))
            price = float(input("Ціна: "))
            orders[num] = [item, qty, price]
            save_orders(orders)

        elif choice == "2":
            for k, v in orders.items():
                print(k, v)

        elif choice == "3":
            num = input("Номер: ")
            print(orders.get(num, "Не знайдено"))

        elif choice == "4":
            num = input("Номер: ")
            if num in orders:
                orders[num][1] = int(input("Нова кількість: "))
                orders[num][2] = float(input("Нова ціна: "))
                save_orders(orders)

        elif choice == "5":
            num = input("Номер: ")
            if num in orders:
                del orders[num]
                save_orders(orders)

        elif choice == "6":
            break

# Завдання 6

students_file = "students.txt"

def load_students():
    if not os.path.exists(students_file):
        return []
    with open(students_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        students = [line.strip().split(";") for line in lines if line.strip()]
    return students

def save_students(students):
    with open(students_file, "w", encoding="utf-8") as f:
        for s in students:
            f.write(";".join(s) + "\n")

def task6():
    while True:
        print("\n1 Додати")
        print("2 Переглянути")
        print("3 Пошук")
        print("4 Оновити")
        print("5 Видалити")
        print("6 Вихід")
        c = input("> ")

        students = load_students()

        if c == "1":
            name = input("Ім'я: ")
            course = input("Курс: ")
            grade = input("Бал: ")
            students.append([name, course, grade])
            save_students(students)

        elif c == "2":
            for s in students:
                print(s)

        elif c == "3":
            name = input("Ім'я: ")
            for s in students:
                if s[0] == name:
                    print(s)

        elif c == "4":
            name = input("Ім'я: ")
            for s in students:
                if s[0] == name:
                    s[1] = input("Новий курс: ")
                    s[2] = input("Новий бал: ")
                    save_students(students)

        elif c == "5":
            name = input("Ім'я: ")
            students = [s for s in students if s[0] != name]
            save_students(students)

        elif c == "6":
            break



