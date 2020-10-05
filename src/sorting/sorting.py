# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here

    while elements >= 2:
        left = arrA[0]
        right = arrB[0]

        if left < right:
            arrA.pop(0)
            merged_arr.append(left)
        if right < left:
            arrB.pop(0)
            merged_arr.append(right)
        
        elements -= 1
    
    if arrA:
        merged_arr.append(arrA)
    else:
        merged_arr.append(arrB)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


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
