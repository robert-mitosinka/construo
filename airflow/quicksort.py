
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Input from user
input_data = [12, 47, 3, 89, 25, 61, 34, 78, 56, 90, 11, 42, 67, 8, 29, 73, 5, 38, 94, 21]
numbers = list(map(int, input_data.split()))

# Sorting
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
