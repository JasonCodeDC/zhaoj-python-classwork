### SRC - This should be in a folder called assessments
### and please use the coding conventions. I have updated Q3 
### as an example.
def Q1():
    a = input()
    print(a[-1] + a[1:-1] + a[0])
# endprocedure

def Q2():
    a = input()
    b = input()
    c = input()
    if c.lower() == "pm":
        print(int(a)*60 + int(b) + 12)
    else:
        print(int(a)*60 + int(b))
    # endif

def Q3():
    a = int(input())
    if a > 600:
        if a % 60 < 10:
            print(f"0{a // 60}:0{a % 60}")
        else:
            print(f"0{a // 60}:{a % 60}")
        #endif
    else:
        if a % 60 < 10:
            print(f"{a // 60}:0{a % 60}")
        else:
            print(f"{a // 60}:{a % 60}")
        # endif
    # endif
# endprocedure

def Q4():
    total = 0
    for _ in range(10):
        total += int(input())
    # next _
    print(f"The total is {total}")
# endprocedure

def Q5():
    total = 0
    count = -1
    a = 0
    while a>= 0:
        total += a
        count += 1
        a = int(input())
    # endwhile
    print(a/count)
# endprocedure

def Q6procedure(arr:list):
    biggest = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
        # endif 
    # next i
    print(biggest)
# endprocedure

def Q6function(arr:list):
    biggest = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
        # endif
    # next i
    return biggest
# endfunction

# largest = Q6function(my_array)

def Q7PartOne(arr:list):
    maximum_num = arr[0][0]
    for array in arr:
        if Q6function(array)> maximum_num:
            maximum_num = Q6function(array)
        # endif
    # next array
    return(maximum_num)
# endfunction


def Q7PartTwo(arr:list):
    highest_data = [arr[0][0], 0, 0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > highest_data[0]:
                highest_data = [arr[i][j], i, j]
            # endif
        # next j
    # next i
    print(f"The highest value is {highest_data[0]} in row {highest_data[1]} column {highest_data[2]}")
# endprocedure

def Q8():
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    a = input()
    for i in range(len(a)):
        if a[i] in "0123456789":
            left = a[:i]
            right = a[i+1:]
            a = f"{left}{numbers[int(a[i])]}{right}"
        # endif
    # next i
    print(a)
# endprocedure