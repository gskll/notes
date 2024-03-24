# Fast: Merge sort is much faster than bubble sort, being O(n*log(n)) instead of O(n^2).
#
# Stable: Merge sort is also a stable sort which means that values with duplicate keys in the original list will be in the same order in the sorted list.
#
# Extra memory: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires an extra array in memory to merge the sorted subarrays.
#
# Recursive: Merge sort requires many recursive function calls, and function calls can have significant resource overhead.


def merge(first: list[int], second: list[int]) -> list[int]:
    res = []
    i, j = 0, 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            res.append(first[i])
            i += 1
        else:
            res.append(second[j])
            j += 1

    if i < len(first):
        res += first[i:]

    if j < len(second):
        res += second[j:]

    return res


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2
    first = nums[:middle]
    second = nums[middle:]

    first_sorted = merge_sort(first)
    second_sorted = merge_sort(second)
    return merge(first_sorted, second_sorted)


# arr = [3, 1, 5, 2]
arr = [3, 2, 1, 5, 2, 6, -1, 32, 12, 9, 4, 5]
merge_sorted = merge_sort(arr)
sorted = sorted(arr)
print("====")
print("arr", arr)
print("got", merge_sorted)
print("expect", sorted)
print(merge_sorted == sorted)
