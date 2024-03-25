class HashMap:
    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)

        load = self.current_load()
        if load < 0.05:
            return

        old = self.hashmap
        self.hashmap = [None for _ in range(len(old) * 10)]
        for x in old:
            if x is None:
                continue
            self.insert(x[0], x[1])

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1

        filled = 0
        for i in self.hashmap:
            if i:
                filled += 1

        return filled / len(self.hashmap)

    def get(self, key):
        index = self.key_to_index(key)
        entry = self.hashmap[index]
        if entry is None:
            raise Exception("sorry, key not found")

        return entry[1]

    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def key_to_index(self, key):
        hash = 0
        for c in key:
            hash += ord(c)
        return hash % len(self.hashmap)

    def __init__(self, size):
        self.hashmap: list[None | tuple[str, object]] = [None for _ in range(size)]

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final


run_cases = [
    (
        [
            ("apple", 1),
            ("banana", 2),
            ("cherry", 3),
            ("mango", 4),
            ("orange", 5),
            ("pear", 6),
            ("plum", 7),
        ],
        [
            (1.0, 1),
            (0.2, 10),
            (0.03, 100),
            (0.03, 100),
            (0.04, 100),
            (0.05, 100),
            (0.006, 1000),
        ],
    )
]

submit_cases = run_cases + [
    (
        [
            ("golang", 1),
            ("python", 2),
            ("javascript", 3),
            ("typescript", 4),
            ("rust", 5),
            ("perl", 6),
            ("java", 7),
            ("sql", 8),
        ],
        [
            (1.0, 1),
            (0.2, 10),
            (0.03, 100),
            (0.04, 100),
            (0.05, 100),
            (0.006, 1000),
            (0.007, 1000),
            (0.008, 1000),
        ],
    )
]


def test(items, expected_outputs):
    hm = HashMap(0)
    print("=====================================")
    actual = []
    for i, item in enumerate(items):
        key = item[0]
        val = item[1]
        expected_load = expected_outputs[i][0]
        expected_size = expected_outputs[i][1]
        print(f"insert({key}, {val})")
        print(f"Expected Load: {expected_load}")
        print(f"Expected Size: {expected_size}")
        try:
            hm.insert(key, val)
            print(f"Actual Load: {hm.current_load()}")
            print(f"Actual Size: {len(hm.hashmap)}")
            print("---------------------------------")
            actual.append((hm.current_load(), len(hm.hashmap)))
        except Exception as e:
            print(f"Error: {e}")
            print("Fail")
    print("=====================================")
    if actual == expected_outputs:
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
