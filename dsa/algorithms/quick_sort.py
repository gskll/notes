# Pros:
#
#     Very fast in the average case
#     In-Place: Saves on memory, doesn't need to do a lot of copying and allocating
#
# Cons:
#
#     More complex implementation
#     Typically unstable: changes the relative order of elements with equal keys

# # On average, quicksort has a Big O of O(n*log(n)). In the worst case, and assuming we don't take any steps to protect ourselves, it can break down to O(n^2).
# #
# # partition() has a single for-loop that ranges from the lowest index to the highest index in the array. By itself, the partition() function is O(n). The overall complexity of quicksort is dependent on how many times partition() is called.
# #
# # In the worst case, the input is already sorted. An already sorted array results in the pivot being the largest or smallest element in the partition each time. When this is the case, partition() is called a total of n times.
# #
# # In the best case, the pivot is the middle element of each sublist which results in log(n) calls to partition().
#
# Fixing Quick Sort Big O
#
# As we discussed, while the version of quicksort that we implemented is almost always able to perform at speeds of O(n*log(n)), its Big O is still technically O(n^2). We can fix this by altering the algorithm slightly.
#
# There are two approaches:
#
#     Shuffle input randomly before sorting. This can trivially be done in O(n) time
#     Actively find the median of a sample of data from the partition, this can be done in O(1) time.
#
# Random Approach
#
# The random approach is easy to code, works practically all of the time, and as such is often used.
#
# The idea is to quickly shuffle the list before sorting it. The likelihood of shuffling into a sorted list is astronomically unlikely, and is also more unlikely the larger the input.
# Median Approach
#
# One of the most popular solutions is to use the "median of three" approach. Three elements (for example: the first, middle, and last elements) of each partition are chosen and the median is found between them. That item is then used as the pivot.
#
# This approach has the advantage that it can't break down to O(n^2) time because we are guaranteed to never use the worst item in the partition as the pivot. That said, it can still be slower because a true median isn't used.


import time


def quick_sort(nums: list[int], low: int, high: int) -> list[int]:
    if low < high:
        nums, index = partition(nums, low, high)
        nums = quick_sort(nums, low, index - 1)
        nums = quick_sort(nums, index + 1, high)

    return nums


def partition(nums: list[int], low: int, high: int) -> tuple[list[int], int]:
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]
    return nums, i


run_cases = [
    ([2, 1, 3], 0, 2, [1, 2, 3]),
    ([9, 6, 2, 1, 8, 7], 0, 5, [1, 2, 6, 7, 8, 9]),
]

submit_cases = run_cases + [
    ([], 0, -1, []),
    ([1], 0, 0, [1]),
    ([1, 2, 3, 4, 5], 0, 4, [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], 0, 4, [1, 2, 3, 4, 5]),
    ([0, 1, 6, 4, 7, 3, 2, 8, 5, -9], 0, 9, [-9, 0, 1, 2, 3, 4, 5, 6, 7, 8]),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    print(f" * low: {input2}")
    print(f" * high: {input3}")
    print(f"Expecting: {expected_output}")
    start = time.time()
    result = input1.copy()
    quick_sort(result, input2, input3)
    end = time.time()
    timeout = 1.00
    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        print(f"Actual: {result}")
        print("Fail")
        return False
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
        print(f"Actual: {result}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
