def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        smallest_i = i

        for j in range(smallest_i + 1, len(nums)):
            if nums[j] < nums[smallest_i]:
                smallest_i = j

        nums[i], nums[smallest_i] = nums[smallest_i], nums[i]

    return nums


run_cases = [
    ([5, 3, 8, 6, 1, 9], [1, 3, 5, 6, 8, 9]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
]

submit_cases = run_cases + [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([15, 12, 8, 7, 5, 3, 1], [1, 3, 5, 7, 8, 12, 15]),
    ([10, 5, 3, 7, 2, 8, 1], [1, 2, 3, 5, 7, 8, 10]),
    ([], []),
    ([1], [1]),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expecting: {expected_output}")
    result = selection_sort(input)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
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
