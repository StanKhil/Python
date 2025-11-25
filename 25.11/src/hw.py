#----------HW1------------
def task1(t1, t2, t3):
    return tuple(set(t1) & set(t2) & set(t3))


def task2(t1, t2, t3):
    s1, s2, s3 = set(t1), set(t2), set(t3)
    u1 = s1 - s2 - s3
    u2 = s2 - s1 - s3
    u3 = s3 - s1 - s2
    return tuple(u1), tuple(u2), tuple(u3)


def task3(t1, t2, t3):
    res = []
    for i in range(min(len(t1), len(t2), len(t3))):
        if t1[i] == t2[i] == t3[i]:
            res.append(t1[i])
    return tuple(res)


print(task1((1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)))
print(task2((1, 2, 3, 4), (3, 4, 5, 6), (5, 6, 7, 8)))
print(task3((1, 2, 3, 4), (0, 2, 3, 5), (9, 2, 3, 1)))
