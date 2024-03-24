import random
import time


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val


run_cases = [
    (10, "Healing Potion", "Bandage"),
    (100, "Bandage", "Bandage"),
    (1000, "Bandage", "Bandage"),
    (10000, "Healing Potion", "Bandage"),
]

submit_cases = run_cases + [
    (12000, "Bandage", "Bandage"),
]


def test(num_items, first_item, last_item):
    print("---------------------------------")
    print(f"Adding {num_items} items to a linked list's head")
    linked_list = LinkedList()
    timeout = 1
    start = time.time()
    for item in get_items(num_items):
        linked_list.add_to_head(Node(item))

    print(f"Adding {num_items} items to a linked list's tail")
    linked_list2 = LinkedList()
    for item in get_items(num_items):
        linked_list2.add_to_tail(Node(item))
    end = time.time()

    print(f"Expecting to complete in less than {timeout * 1000} milliseconds")
    if (end - start) < timeout:
        print(f"Test completed in less than {timeout * 1000} milliseconds!")
    else:
        print("Fail")
        print(f"Test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
        return False

    print("\nChecking the first linked list")
    if not check_links(linked_list, first_item, last_item, num_items):
        return False
    print("\nChecking the second linked list")
    if not check_links(linked_list2, last_item, first_item, num_items):
        return False

    print("\nPass")
    return True


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


def get_items(num):
    random.seed(1)
    options = ["Healing Potion", "Bandage", "Bronze Shortsword", "Bronze Gloves"]
    items = []
    for _ in range(num):
        optionI = random.randint(0, len(options) - 1)
        items.append(options[optionI])
    return items


def check_links(llist, head, tail, expected_length):
    print(f"Expected Head: {head}")
    print(f"Actual Head: {llist.head}")
    if head != llist.head.val:
        print("Fail")
        print("The linked list's head node does not have the expected value")
        print("Check if nodes added to the head are set as the new head node")
        return False
    print(f"Expected Tail: {tail}")
    print(f"Actual Tail: {llist.tail}")
    if tail != llist.tail.val:
        print("Fail")
        print("The linked list's tail node does not have the expected value")
        print("Check if nodes added to the tail are set as the new tail node")
        return False

    actual_length = 0
    for _ in llist:
        actual_length += 1
    print(f"Expected Length: {expected_length}")
    print(f"Actual Length: {actual_length}")
    if expected_length != actual_length:
        print("Fail")
        print("The linked list is not the expected length of linked nodes")
        print("Check if added nodes are set as the new head or tail")
        return False
    return True


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
