# Given an array of n elements, the task is to return the count of the number of odd numbers in the array.

# Examples
# Example 1:

# Input: n=5, array = [1,2,3,4,5]
# Output: 3

def countodd(n,arr):
    odd_count=0
    for i in arr:
        if i%2==0:
            odd_count+=1
    return odd_count
print(countodd(5,[1,2,3,4,5]))