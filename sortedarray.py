# Given an array arr of size n, the task is to check if the given array is sorted in ascending (increasing or non-decreasing) order. If the array is sorted, return True; otherwise, return False.

# Examples:
# Example 1:
# Input:
# n = 5
# arr = [1, 2, 3, 4, 5]
# Output:
# True
def sortedarr(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print(sortedarr([1,2,3,4,5]))