def fibonacci(n):
    # Write your code here.
    fib0, fib1 = 0, 1
    for i in range(n-1):
        if i % 2 == 0:
            fib0 = fib0 + fib1
        else:
            fib1 = fib0 + fib1
    return fib0 if n % 2 == 0 else fib1
    
n = int(input())
print(fibonacci(n))
