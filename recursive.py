def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


n = 1700
try:
    print(f"The factorial of {n} is {recursive_factorial(n)}")
except RecursionError:
    print(f"Recursion overflow occurred at n = {n}")




import time

start_time = time.time()
recursive_factorial(n)
end_time = time.time()
print(f"Recursive factorial took {end_time - start_time} seconds")
