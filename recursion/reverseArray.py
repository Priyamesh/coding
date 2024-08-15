# two variable approach
# def helper(l, r, arr):
#     if l >= r:
#         return

#     arr[l], arr[r] = arr[r], arr[l]
#     helper(l + 1, r - 1, arr)


# one variable approach
def helper(idx, arr):
    if idx >= len(arr) - 1 - idx:
        return

    arr[idx], arr[len(arr) - 1 - idx] = arr[len(arr) - 1 - idx], arr[idx]
    helper(idx + 1, arr)


def reverseArray():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(arr)
    # helper(0, len(arr) - 1, arr)
    helper(0, arr)
    print(arr)


reverseArray()
