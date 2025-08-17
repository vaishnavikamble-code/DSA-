def duplicate(arr):
    dupli =[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j] and arr[i] not in dupli:
                dupli.append(arr[i])
    return dupli
arr = duplicate([1,3,1,3,4])
print(arr)

OUTPUT: [1,3]
