class LLQueue:
    def __init__(self):
        self.tail = None
        self.head = None

    def remove_from_head(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return node

    def add_to_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


run_cases = [
    (
        ["Dagger", "Spear", "Staff", "Axe", "Bow", "Sword"],
        (["Spear", "Staff", "Axe", "Bow", "Sword"], "Dagger", "Sword"),
    ),
    (
        ["Spear", "Staff", "Axe", "Bow", "Sword"],
        (["Staff", "Axe", "Bow", "Sword"], "Spear", "Sword"),
    ),
    (["Staff", "Axe", "Bow", "Sword"], (["Axe", "Bow", "Sword"], "Staff", "Sword")),
]

submit_cases = run_cases + [
    (["Axe"], ([], "Axe")),
    (["Axe", "Bow", "Sword"], (["Bow", "Sword"], "Axe", "Sword")),
    (["Bow", "Sword"], (["Sword"], "Bow", "Sword")),
    (["Sword"], ([], "Sword")),
    ([], ([],)),
    ([], ([],)),
]


def test(linked_list, expected_state, expected_head=None, expected_tail=None):
    print("---------------------------------")
    print(f"Linked List Queue: {linked_list}")
    print(f"Removing Head...\n")
    try:
        head = linked_list.remove_from_head()
        tail = linked_list.tail
        result = linked_list_to_list(linked_list)
        print(f"Expected List: {expected_state}")
        print(f"  Actual List: {result}\n")
        if result != expected_state:
            print("Fail")
            return False
        print(f"Expected Head: {expected_head}")
        print(f"  Actual Head: {head}\n")
        if not (head == None and expected_head == None) and (head.val != expected_head):
            print("Fail")
            return False
        print(f"Expected Tail: {expected_tail}")
        print(f"  Actual Tail: {tail}\n")
        if not (tail == None and expected_tail == None) and (tail.val != expected_tail):
            print("Fail")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Exception: {str(e)}")
        print("Fail")
        return False


def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)

    return result


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        linked_list = LLQueue()
        for item in test_case[0]:
            linked_list.add_to_tail(Node(item))
        correct = test(linked_list, *test_case[1])
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
