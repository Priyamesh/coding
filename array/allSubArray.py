def printAllSubArray(nums):
    n = len(nums)

    # Loop to set the starting point
    for start in range(n):

        # Loop to set the ending point
        for end in range(start, n):

            # Print subarray from start to end
            print(nums[start : end + 1])


nums = [1, 4, -9, 7, 9, 23, 78, -56]
printAllSubArray(nums)
