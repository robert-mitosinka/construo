# QUICKSORT big time
def quick_sort(in_array):
    if len(in_array) <= 1:
        return in_array

    pivot = in_array[len(in_array) // 2]
    left = [x for x in in_array if x < pivot]
    middle = [x for x in in_array if x == pivot]
    right = [x for x in in_array if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
