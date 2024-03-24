def is_balanced(input_str):
    s = Stack()
    for c in input_str:
        if c == "(":
            s.push(c)
        elif c == ")":
            if s.pop() != "(":
                return False

    return s.peek() == None


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


run_cases = [
    ("(", False),
    ("()", True),
    ("(())", True),
]

submit_cases = run_cases + [
    ("()()", True),
    ("(()))", False),
    ("((())())", True),
    ("(()(()", False),
    (")(", False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_balanced(input1)
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
