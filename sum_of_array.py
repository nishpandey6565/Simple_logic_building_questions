#Given an array arr of size n, your task is to find the sum of all the elements in the array.

# Examples
# Input:
# {"n": 5, "arr": [1, 2, 3, 4, 5]}
# Output:
# 15
def sum_of_array(n,arr):
    sum_of_list=0
    for i in arr:
        sum_of_list+=i
    return
print(sum_of_array([1,2,3,4,5]))