def firstTask(start, end):
    if start >= end:
        tmp = start
        start = end
        end = tmp
    mult = 1
    for i in range(start, end):
        mult *= i
    return mult

#print(firstTask(5, 2))

def secondTask(list1):
    max_value = list1[0]
    for i in list1:
        if i > max_value:
            max_value = i
    return max_value

#print(secondTask([1, 5, 3, 9, 2]))

def thirdTask(list1):
    sum_value = 0
    for i in list1:
        sum_value += i
    return sum_value 

#print(thirdTask([1, 2, 3, 4, 5]))

def fourthTask(list1):
    count_even = 0
    count_positive = 0
    count_negative = 0
    for i in list1:
        if i % 2 == 0:
            count_even += 1
        if i > 0:
            count_positive += 1
        elif i < 0:
            count_negative += 1
    return count_even, len(list1) - count_even, count_positive, count_negative

#print(fourthTask([1, -2, 3, 4, -5, 6, -7, 8, 0]))

def fifthTask(list1):
    reversed_list = list1[::-1]
    return reversed_list

#print(fifthTask([1, 2, 3, 4, 5]))

def sixthTask(list1):
    factorials = []
    for i in list1:
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        factorials.append(fact)
    return factorials

print(sixthTask([3, 4, 5]))