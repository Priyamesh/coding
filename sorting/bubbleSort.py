"""
Bubble Sort

Step 1: iterate from 0 -> n-1
Step 2: iterate from 0 -> n-i-2
Step 3: check from adj compariosn
        arr[j] > arr[j-1]
        if yes, swap
step 4: if there is no swap in 1st iteration it means 

"""


def bubbleSort(arr):
    n = len(arr)
    swap = False

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        print("i = ", i, arr)
        if not swap:
            break


arr = [87, 65, 4, 9, 54, 52, 85, 49]

print(arr)
bubbleSort(arr)
print(arr)
