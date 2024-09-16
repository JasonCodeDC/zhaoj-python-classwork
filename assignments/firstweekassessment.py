def Q1():
    a = input()
    print(a[-1] + a[1:-1] + a[0])

def Q2():
    a = input()
    b = input()
    c = input()
    if c.lower() == "pm":
        print(int(a)*60 + int(b) + 12)
    else:
        print(int(a)*60 + int(b))

def Q3():
    a = int(input())
    if a > 600:
        if a % 60 < 10:
            print(f"0{a // 60}:0{a % 60}")
        else:
            print(f"0{a // 60}:{a % 60}")
    else:
        if a % 60 < 10:
            print(f"{a // 60}:0{a % 60}")
        else:
            print(f"{a // 60}:{a % 60}")

def Q4():
    total = 0
    for _ in range(10):
        total += int(input())
    print(f"The total is {total}")

def Q5():
    total = 0
    count = -1
    a = 0
    while a>= 0:
        total += a
        count += 1
        a = int(input())
    print(a/count)

def Q6(arr:list):
    biggest = arr[0]
    for i in range(0, len(arr)):
        if arr[i]>biggest:
            biggest = arr[i]
    print(biggest)
    # return(biggest)

# print(Q6(my_array))

def Q7PartOne(arr:list):
    maximum_num = arr[0][0]
    for array in arr:
        if Q6(array)> maximum_num:
            maximum_num = Q6(array)
    return(maximum_num)

def Q7PartTwo(arr:list):
    highest_data = [arr[0][0], 0, 0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > highest_data[0]:
                highest_data = [arr[i][j], i, j]
    print(f"The highest value is {highest_data[0]} in row {highest_data[1]} column {highest_data[2]}")

def Q8():
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    a = input()
    for i in range(len(a)):
        if a[i] in "0123456789":
            left = a[:i]
            right = a[i+1:]
            a = f"{left}{numbers[int(a[i])]}{right}"
    print(a)