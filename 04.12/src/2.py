def convert(num, cof):
    try:
        if num == 0:
            raise ValueError("Num = 0")
        elif num < 0:
            raise ValueError("Num < 0")
        elif num > 100000000:
            raise ValueError("Num too big")
        else:
            return num * cof
    except Exception as e:
        return e
    finally:
        print("end")

print(convert(1, 0.05))
print(convert(0, 10))
print(convert(100000000000000000000000, 0))
