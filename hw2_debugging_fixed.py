"""imports"""
import rand
import trace

def merge_sort(arr):
    """Defines the merge sort function and splits the array in two parts recursively"""
    if (arr == []):
        return arr
    if (len(arr) == 1):
        return arr
    half = len(arr)//2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """Recombines the left and right array to give a sorted array in the end"""
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])
    return merge_arr


inp_arr = rand.random_array([None] * 20)
arr_out = merge_sort([inp_arr])

print(arr_out)