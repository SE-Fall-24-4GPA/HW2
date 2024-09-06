"""imports"""

import trace
import rand

def merge_sort(new_arr):
    """Defines the merge sort function and splits the array in two parts"""
    if len(new_arr) == 1:
        return new_arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))

def recombine(left_arr, right_arr):
    """Recombines the arrays"""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr

def custom_trace_func(frame, event, arg):
    """create tracer function"""
    with open("trace_log.txt", "a") as f:

        f.write(f"{frame.f_code.co_filename}:{frame.f_lineno} - {event}\n")

    return


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)

tracer = trace.Tracer(tracefunc=custom_trace_func)
tracer.run('your_function()')
