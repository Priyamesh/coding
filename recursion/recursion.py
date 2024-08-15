# Parameterised way

# def helper(n, sum):
#     if n == 0:
#         return
#     sum[0] += n
#     helper(n - 1, sum)


# def sumOfNumber(n):
#     sum = [0]
#     helper(n, sum)
#     return sum[0]


# functional way
def helper(n):
    if n == 1:
        return 1
    return n + helper(n - 1)


def sumOfNumber(n):
    return helper(n)


print(sumOfNumber(5))
