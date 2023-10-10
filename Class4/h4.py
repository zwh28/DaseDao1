def select_sort(array):
    for i in range(len(array)):
        x=i
        for j in range(i, len(array)):
            if array[j]<array[x]:
                x=j
        array[i],array[x]=array[x],array[i]
    return array
arr = list(input("请输入一个数组\n").split(" "))
select_sort(arr)
print(arr)