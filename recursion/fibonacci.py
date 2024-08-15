def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))

# TC: O(2^n) Exponetial
# SC: O(n)
