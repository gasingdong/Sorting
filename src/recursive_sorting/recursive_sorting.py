# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    lengthA = len(arrA)
    lengthB = len(arrB)
    elements = lengthA + lengthB
    merged_arr = [0] * elements
    # TO-DO
    indexA = 0
    indexB = 0
    for i in range(0, elements):
        if indexA >= lengthA or (indexB < lengthB
                                 and arrA[indexA] >= arrB[indexB]):
            merged_arr[i] = arrB[indexB]
            indexB += 1
        else:
            merged_arr[i] = arrA[indexA]
            indexA += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    needs_sort = True
    while needs_sort:
        needs_sort = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                needs_sort = True


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if (r - l) >= 2:
        middle = (l + r)//2
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle, r)
        merge_in_place(arr, l, middle, r)
    return arr


# STRETCH: implement the Timsort function below
# hint:
# check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
