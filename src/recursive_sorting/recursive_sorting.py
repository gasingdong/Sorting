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
    for x in range(mid + 1, end + 1):
        for y in range(start, mid + 1):
            if arr[x] < arr[y]:
                arr.insert(y, arr[x])
                arr.pop(x + 1)
                mid += 1


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l < r:
        middle = (l + r)//2
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)
        merge_in_place(arr, l, middle, r)
    return arr


# STRETCH: implement the Timsort function below
# hint:
# check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    if not arr:
        return arr

    runs = []
    minrun = 4
    start = 0
    index = 0
    direction = 0

    while index < len(arr):
        end_run = False

        if index > len(arr) - 1:
            element = arr[index]
            next_element = arr[index + 1]

            if direction == 0:
                if element < next_element:
                    direction = 1
                elif element > next_element:
                    direction = -1
            elif direction == 1:
                if element > next_element:
                    end_run = True
            elif direction == -1:
                if element < next_element:
                    end_run = True
        else:
            end_run = True

        index += 1

        if end_run:
            while (index - start) < minrun and index < len(arr):
                index += 1

            run_arr = arr[start:index]

            for i in range(1, len(run_arr)):
                element = run_arr[i]
                j = i
                while j > 0 and element < run_arr[j - 1]:
                    run_arr[j] = run_arr[j - 1]
                    j -= 1
                run_arr[j] = element
            runs.append(run_arr)
            start = index

    if start < len(arr):
        runs.append(arr[start:])

    def merge_arr(arr_inner):
        if len(arr_inner) <= 1:
            return arr_inner
        result = []

        while len(arr_inner) > 1:
            result.append(merge(arr_inner.pop(), arr_inner.pop()))

        if arr_inner:
            result.append(arr_inner.pop())
        return merge_arr(result)

    return merge_arr(runs)
