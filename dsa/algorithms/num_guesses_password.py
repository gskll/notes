# Complete the get_num_guesses function. It takes a password length as input and returns the number of guesses required to ensure that a password of that length or shorter is guessed.


def get_num_guesses(length):
    seen = {0: 0}

    curr = 0
    for i in range(1, length + 1):
        curr = (26**i) + seen[i - 1]
        seen[i] = curr

    return curr


run_cases = [
    (1, 26),
    (2, 702),
    (3, 18278),
]

submit_cases = run_cases + [
    (4, 475254),
    (5, 12356630),
    (6, 321272406),
    (7, 8353082582),
    (8, 217180147158),
    (9, 5646683826134),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = get_num_guesses(input)
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
