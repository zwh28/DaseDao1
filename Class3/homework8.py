import random
import time
def creatarray(k):
    arr=[random.randint(1,10000) for _ in range(k)]
    return arr

def Partition(arr, p, r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<x:
            i += 1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def quicksort(arr,p,r):
    if p<r:
        q=Partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)
    return

def select_sort(array):
    for i in range(len(array)):
        x=i
        for j in range(i, len(array)):
            if array[j]<array[x]:
                x=j
        array[i],array[x]=array[x],array[i]
    return array


def merge_sort(array):
    if len(array) == 1:
        return array
    left_array = merge_sort(array[:len(array) // 2])
    right_array = merge_sort(array[len(array) // 2:])
    return merge(left_array, right_array)


def merge(left_array, right_array):
    left_index, right_index, merge_array = 0, 0, list()
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            merge_array.append(left_array[left_index])
            left_index += 1
        else:
            merge_array.append(right_array[right_index])
            right_index += 1
    merge_array = merge_array + left_array[left_index:] + right_array[right_index:]
    return merge_array

for k in [10,100,1000]:
    arr=creatarray(k)
    temp1=arr
    temp2=arr
    temp3=arr
    start_time1 = time.time()
    select_sort(temp1)
    end_time1 = time.time()
    start_time2 = time.time()
    merge_sort(temp2)
    end_time2 = time.time()
    start_time3 = time.time()
    quicksort(temp3, 0, len(arr) - 1)
    end_time3 = time.time()
    print("数组长度：%d"%k )
    print("选择排序时间：%f"%(end_time1-start_time1))
    print("归并排序时间：%f"%(end_time2-start_time2))
    print("快速排序时间：%f"%(end_time3-start_time3))


        