def helper(l, r, st):
    if l >= r:
        return True

    return st[l] == st[r] and helper(l + 1, r - 1, st)


def checkPalindrome(st):
    res = helper(0, len(st) - 1, st)
    print(res)


checkPalindrome("abbbav")
checkPalindrome("vabbbav")
