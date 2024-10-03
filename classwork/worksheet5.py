def recur_fib(n:int) -> int:
    if n <= 1:
        return n
    else:
        return recur_fib(n - 1) + recur_fib(n - 2)

def iter_fib(n:int) -> int:
    num1 = 1
    num2 = 1
    for _ in range(n-2 if n >= 2 else 0):
        temp = num2
        num2 += num1
        num1 = temp
    return num2


if __name__ == "__main__":
    import time
    import random

    NUM_TESTS = 10
    MIN_NUM = 5
    MAX_NUM = 10

    nums = [random.randint(MIN_NUM, MAX_NUM) for _ in range(NUM_TESTS)]
    recur_times = []
    iter_times = []
    recur_results = []
    iter_results = []

    for i in range(NUM_TESTS):
        print(f"Recursive test {i+1}")
        time1 = time.perf_counter()
        result = recur_fib(nums[i])
        time2 = time.perf_counter()
        recur_times.append(time2-time1)
        recur_results.append(result)

    for i in range(NUM_TESTS):
        print(f"Iterative test {i+1}")
        time1 = time.perf_counter()
        result = iter_fib(nums[i])
        time2 = time.perf_counter()
        iter_times.append(time2-time1)
        iter_results.append(result)
    
    recur_avg = sum(recur_times) / NUM_TESTS
    iter_avg = sum(iter_times) / NUM_TESTS

    print(f"{nums}")
    # print(f"Iterative results: {iter_results}\nIterative times: {iter_times}\nIterative average: {sum(iter_times) / NUM_TESTS}")
    # print(f"Recursive results: {recur_results}\nRecursive times: {recur_times}\nRecursive average: {sum(recur_times) / NUM_TESTS}")
    print((f"Iterative is faster by {recur_avg - iter_avg}" if iter_avg < recur_avg 
           else f"Recursive is faster by {iter_avg - recur_avg}") if recur_results == iter_results 
           else f"Test invalid")