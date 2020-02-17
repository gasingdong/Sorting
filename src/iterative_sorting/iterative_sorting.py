# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        lowest_idx = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_idx]:
                lowest_idx = j
        # TO-DO: swap
        arr[i], arr[lowest_idx] = arr[lowest_idx], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    needs_sort = True
    while needs_sort:
        needs_sort = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                needs_sort = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if not arr:
        return arr

    limit = maximum
    if limit == -1:
        for num in arr:
            if num > limit:
                limit = num

    count = [0] * (limit + 1)
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[num] += 1

    total = 0
    for i in range(0, len(count)):
        total = count[i] + total
        count[i] = total

    result = [0] * len(arr)
    for num in arr:
        result[count[num] - 1] = num
        count[num] = count[num] - 1

    return result
