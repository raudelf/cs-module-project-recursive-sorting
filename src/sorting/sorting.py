# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here

    while elements:

        if arrA and arrB:
            if arrA[0] < arrB[0]:
                merged_arr.append(arrA[0])
                arrA.pop(0)
                elements -= 1
            else:
                merged_arr.append(arrB[0])
                arrB.pop(0)
                elements -= 1
        else:
            if arrA:
                merged_arr.append(arrA[0])
                arrA.pop(0)
                elements -= 1
            if arrB:
                merged_arr.append(arrB[0])
                arrB.pop(0)
                elements -= 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge(left, right)
        return arr
    else:
        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
