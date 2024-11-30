def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = 1600
try:
    print(f"The factorial of {n} is {iterative_factorial(n)}")
except OverflowError:
    print(f"Overflow occurred at n = {n}")


import time

start_time = time.time()
iterative_factorial(n)
end_time = time.time()
print(f"Iterative factorial took {end_time - start_time} seconds")


