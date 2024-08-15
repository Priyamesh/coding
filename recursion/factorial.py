def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(6))

# TC : O(n)
# SC : O(n)
