"""
Insertion Sort

Step1: iterate i from 0 -> n-1
Step2: iterate j from i -> 0
Step3: check and swap

"""


def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i, 0, -1):
            print(j)
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

        print("i = ", i, arr)


arr = [23, 6, 89, 45, 923, 49, 12]

print(arr)
insertionSort(arr)
print(arr)
