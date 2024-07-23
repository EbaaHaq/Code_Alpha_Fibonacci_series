print("TASK1 \n CodeAlpha_fibonacci_generator")

def fibonacci_generator():
    a, b = 0, 1
    while a <= 100:
        print(f"{a} + {b} = {a + b}")
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = fibonacci_generator()
fib_series = []
for num in fib_gen:
    fib_series.append(num)

print("\nFibonacci series up to 100:")
print(fib_series)
