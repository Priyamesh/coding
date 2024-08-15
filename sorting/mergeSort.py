"""
Merge Sort

step1: divide the array into 2 half
step2: make recursive call for both the half
step3: join them

"""

# TC : O(NlogN)
# SC : O(n)


def merge(low, mid, high, arr):
    left = low
    right = mid + 1
    temp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def divide(low, high, arr):

    if low == high:
        return

    mid = (low + high) // 2

    divide(low, mid, arr)
    divide(mid + 1, high, arr)
    merge(low, mid, high, arr)


def mergeSort(arr):
    divide(0, len(arr) - 1, arr)


arr = [87, 66, 1, 23, 90, 77]
mergeSort(arr)
print(arr)
