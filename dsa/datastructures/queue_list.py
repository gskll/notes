class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items = [item] + self.items

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
    ("push", "Bow", ["Bow"], None),
    ("push", "Sword", ["Sword", "Bow"], None),
    ("peek", None, ["Sword", "Bow"], "Bow"),
    ("size", None, ["Sword", "Bow"], 2),
    ("pop", None, ["Sword"], "Bow"),
]

submit_cases = run_cases + [
    ("push", "Shield", ["Shield", "Sword"], None),
    ("peek", None, ["Shield", "Sword"], "Sword"),
    ("size", None, ["Shield", "Sword"], 2),
    ("pop", None, ["Shield"], "Sword"),
    ("pop", None, [], "Shield"),
    ("size", None, [], 0),
    ("pop", None, [], None),
    ("peek", None, [], None),
]


def test(queue, method, input, expected_state, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Queue: {queue.items}")
    print(f" * Method: {method}")
    print(f" * Item (only for push): {input}")
    print(f"Expected Return: {expected_output}")
    print(f"Expected Queue: {expected_state}")
    queue_method = getattr(queue, method)
    if input:
        result = queue_method(input)
    else:
        result = queue_method()
    print(f"Actual Return: {result}")
    print(f"Actual Queue: {queue.items}")
    if result == expected_output and queue.items == expected_state:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    queue = Queue()
    for test_case in test_cases:
        correct = test(queue, *test_case)
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
