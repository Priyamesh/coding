"""
Selection Sort

step 1: iterate i for 1 -> n
step 2: iterate inner loop from i -> n
step 3: check for smallest number from i -> n
step 4: swap the ith pos number with the smallest number
"""

# TC: O(n)
# SC: O(1)


def selectonSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        print("i = ", i, arr)


arr = [108, 56, 98, 12, 23]

print(arr)
selectonSort(arr)
print(arr)
