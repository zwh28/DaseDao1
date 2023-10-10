def insertion_sort(arr):
    for i in range(len(arr)):
        j = i - 1
        current = int(arr[i])
        while j >= 0 and int(arr[j]) > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


arr = list(input("请输入一个数组\n").split(" "))
insertion_sort(arr)
print(arr)
