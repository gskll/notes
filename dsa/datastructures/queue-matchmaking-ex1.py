# Complete the matchmake function that simulates players joining and leaving the matchmaking queue. The function should take a queue instance and a player tuple containing a name and action (either "join" or "leave"):
#
# player = ('Bob', 'join')
# player = ('Alice', 'leave')


def matchmake(queue, player) -> str:
    action = player[1]
    match action:
        case "join":
            queue.push(player[0])
        case "leave":
            queue.search_and_remove(player[0])

    if queue.size() < 4:
        return "No match found"

    p1 = queue.pop()
    p2 = queue.pop()
    return f"{p1} matched {p2}!"


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"


run_cases = [
    [("Alice", "join"), (["Alice"], "No match found")],
    [("Bob", "join"), (["Bob", "Alice"], "No match found")],
    [("Charlie", "join"), (["Charlie", "Bob", "Alice"], "No match found")],
    [("David", "join"), (["David", "Charlie"], "Alice matched Bob!")],
    [("Eve", "join"), (["Eve", "David", "Charlie"], "No match found")],
    [("Frank", "join"), (["Frank", "Eve"], "Charlie matched David!")],
    [("Frank", "leave"), (["Eve"], "No match found")],
    [("Eve", "leave"), ([], "No match found")],
]

submit_cases = run_cases + [
    [("Kevin", "join"), (["Kevin"], "No match found")],
    [("Kevin", "leave"), ([], "No match found")],
    [("John", "join"), (["John"], "No match found")],
    [("Cranston", "join"), (["Cranston", "John"], "No match found")],
    [("Liz", "join"), (["Liz", "Cranston", "John"], "No match found")],
    [("Brett", "join"), (["Brett", "Liz"], "John matched Cranston!")],
]


def test(queue, player, expected_state):
    print("---------------------------------")
    print(f"Queue: {queue}")
    name = player[0]
    action = player[1]
    if action == "leave":
        print(f"{name} left the queue.")
    if action == "join":
        print(f"{name} joined the queue.")
    print(f"Expecting Queue: {expected_state[0]}")
    print(f"Expecting Return: {expected_state[1]}")
    try:
        result = matchmake(queue, player)
    except Exception as e:
        result = f"Error: {e}"
    print(f"Actual Queue: {queue}")
    print(f"Actual Return: {result}")
    if result == expected_state[1] and queue.items == expected_state[0]:
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
