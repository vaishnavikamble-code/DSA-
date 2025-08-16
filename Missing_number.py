def missing(arr):
    max_value = max(arr)
    min_value=min(arr)
    n = max_value - min_value + 1
    total = n*(min_value+max_value)//2
    missing_val = total - sum(arr)
    return missing_val
arr = missing([1,2,3,5])
print(arr)
