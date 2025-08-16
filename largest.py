def largest(arr):
    max_ele=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_ele:
            max_ele = arr[i]
    return max_ele
arr = largest([1,2,3,4,5])
print(arr)  #5


def second_largest(arr):
    max_ele=arr[0]
    for i in range(len(arr)-1):
        if arr[i]>max_ele:
            max_ele = arr[i]
    return max_ele
arr = second_largest([10,20,3,45,99])
print(arr)   #4
