def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

fib8 = [
    fibonacci(0),
    fibonacci(1),
    fibonacci(2),
    fibonacci(3),
    fibonacci(4),
    fibonacci(5),
    fibonacci(6),
]

print(fib8)