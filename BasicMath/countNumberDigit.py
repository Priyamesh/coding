def countDigit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


res = countDigit(987654321)
print(res)
