class Stack:
    def __init__(self):
        self.items = []

    def push(self, arrow):
        self.items.append(arrow)

    def pop(self):
        if not self.size():
            return None

        return self.items.pop()

    def peek(self):
        if not self.size():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


run_cases = [
    ("push", "Fire arrow", ["Fire arrow"], None),
    ("push", "Lightning arrow", ["Fire arrow", "Lightning arrow"], None),
    ("peek", None, ["Fire arrow", "Lightning arrow"], "Lightning arrow"),
    ("size", None, ["Fire arrow", "Lightning arrow"], 2),
    ("pop", None, ["Fire arrow"], "Lightning arrow"),
]

submit_cases = run_cases + [
    ("push", "Ice arrow", ["Fire arrow", "Ice arrow"], None),
    ("peek", None, ["Fire arrow", "Ice arrow"], "Ice arrow"),
    ("size", None, ["Fire arrow", "Ice arrow"], 2),
    ("pop", None, ["Fire arrow"], "Ice arrow"),
    ("pop", None, [], "Fire arrow"),
    ("pop", None, [], None),
    ("peek", None, [], None),
    ("size", None, [], 0),
]


def test(stack, method, input, expected_state, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Stack: {stack.arrows}")
    print(f" * Method: {method}")
    print(f" * Item (only for push): {input}")
    print(f"Expected Return: {expected_output}")
    print(f"Expected Stack: {expected_state}")
    stack_method = getattr(stack, method)
    if input:
        result = stack_method(input)
    else:
        result = stack_method()
    print(f"Actual Return: {result}")
    print(f"Actual Stack: {stack.arrows}")
    if result == expected_output and stack.arrows == expected_state:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    stack = Stack()
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(stack, *test_case)
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
