def gcd(n, m):

    # brute-force
    # r = min(n, m)
    # for i in range(r, 0, -1):
    #     if n % i == 0 and m % i == 0:
    #         return i

    # Euclidean Algorithm
    """
    gcd(n,m) = gcd(n-m, m)  where n>m

    another better:
    gcd(n,m) -> gcd(m, n%m) till m becomes 0

    TC : O(log i (min(n,m)))
    """
    if m == 0:
        return n
    return gcd(m, n % m)


res = gcd(12, 15)
print(res)
