# We know that TSP takes factorial time to solve. The reason is that we need to try every permutation of all the possible cities. For example, given 4 cities, A, B, C, D, we need to try 24 permutations
#
# Even though it takes factorial time to solve TSP, TSP is in NP because we can verify a solution much faster.


# O(n)
def verify_tsp(paths: list[list[int]], dist: int, actual_path: list[int]) -> bool:
    actual_dist = 0
    for step in range(1, len(actual_path)):
        actual_dist += paths[actual_path[step - 1]][actual_path[step]]

        if actual_dist >= dist:
            return False

    if actual_dist < dist:
        return True

    return False


run_cases = [
    ([[0, 394], [394, 0]], [0, 1], 3458, True),
    ([[0, 911, 430], [911, 0, 41], [430, 41, 0]], [1, 2, 0], 3104, True),
]

submit_cases = run_cases + [
    (
        [
            [0, 988, 523, 497],
            [988, 0, 414, 940],
            [523, 414, 0, 802],
            [497, 940, 802, 0],
        ],
        [1, 0, 2, 3],
        1060,
        False,
    ),
    (
        [
            [0, 310, 991, 488, 366],
            [310, 0, 597, 913, 929],
            [991, 597, 0, 223, 516],
            [488, 913, 223, 0, 142],
            [366, 929, 516, 142, 0],
        ],
        [0, 1, 3, 4, 2],
        3399,
        True,
    ),
    (
        [
            [0, 143, 773, 97, 633, 818],
            [143, 0, 256, 931, 545, 722],
            [773, 256, 0, 829, 616, 923],
            [97, 931, 829, 0, 150, 317],
            [633, 545, 616, 150, 0, 101],
            [818, 722, 923, 317, 101, 0],
        ],
        [0, 3, 2, 4, 5, 1],
        1480,
        False,
    ),
]


def print_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        print(mat[i])


def test(paths, actual_path, dist, expected_output):
    try:
        print("---------------------------------")
        print(f"Paths:")
        print_matrix(paths)
        print(f"Checking for a path shorter than {dist}")
        print(f"Using path: {actual_path}")
        print(f"Expecting: {expected_output}")
        result = verify_tsp(paths, dist, actual_path)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
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
