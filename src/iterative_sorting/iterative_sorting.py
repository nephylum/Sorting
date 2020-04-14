# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1 ,len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if arr[smallest_index] < arr[cur_index]:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #loop through array break when there is no change
    change = True
    # cur_index = 0
    while change == True:
        if change == True:
            cur_index = 0
        change = False

        for x in range(cur_index + 1, len(arr)):
            print(arr)
            print(cur_index, arr[cur_index], x, arr[x])
            if arr[x] < arr[cur_index]:
                arr[cur_index], arr[x] = arr[x], arr[cur_index]
                change = True
            cur_index += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

print(bubble_sort([1,3,2,4,5,0]))
