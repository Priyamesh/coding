def checkForPrime(n):

    # for i in range(2, n):
    #     if n % i == 0:
    #         return False
    # return True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


res = checkForPrime(17)
print(res)
