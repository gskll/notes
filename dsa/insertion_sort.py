# Simple implementation, easy to write
# Fast for very small data sets
# Faster than other simple sorting algorithms like Bubble Sort
# Adaptive: Faster for partially sorted data sets
# Stable: Does not change the relative order of elements with equal keys
# In-Place: Only requires a constant amount of memory
# Online: Can sort a list as it receives it

# Some production sorting implementations use insertion sort for very small inputs under a certain threshold (very small, like 10-ish). Insertion sort is better for very small lists than some of the faster algorithms because:
# - There is no recursion overhead
# - Tiny memory footprint
# - It's a stable sort as described above


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i

        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1

    return nums


# arr = [3, 1, 5, 2]
arr = [3, 2, 1, 5, 2, 6, -1, 32, 12, 9, 4, 5]
merge_sorted = insertion_sort(arr)
sorted = sorted(arr)
print("====")
print("arr", arr)
print("got", merge_sorted)
print("expect", sorted)
print(merge_sorted == sorted)
