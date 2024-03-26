import json


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def exists(self, word):
        current = self.root

        for c in word:
            if c not in current:
                return False
            current = current[c]

        return self.end_symbol in current

    def add(self, word):
        current = self.root

        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current[self.end_symbol] = True

    def words_with_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur:
                return []
            cur = cur[c]

        return self.search_level(cur, prefix, [])

    def search_level(self, cur: dict[str, dict], cur_prefix: str, words: list[str]):
        if self.end_symbol in cur:
            words.append(cur_prefix)

        level_chars = sorted(cur.keys())
        for c in level_chars:
            if c != self.end_symbol:
                self.search_level(cur[c], cur_prefix + c, words)

        return words

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                c = document[j]
                if c not in level:
                    break
                level = level[c]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])

        return matches

    def longest_common_prefix(self):
        cur = self.root
        prefix = ""
        while True:
            children = cur.keys()
            if len(children) != 1:
                break

            c = list(children)[0]
            if c == self.end_symbol:
                break
            prefix += c
            cur = cur[c]
        return prefix

    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                c = document[j]
                if c in variations:
                    c = variations[c]
                if c not in level:
                    break
                level = level[c]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches


run_cases = [
    (
        [
            "darn",
            "nope",
            "bad",
        ],
        "This is a d@rn1t test with b@d words!",
        {
            "@": "a",
            "1": "i",
            "4": "a",
            "!": "i",
        },
        [
            "b@d",
            "d@rn",
        ],
    ),
    (
        [
            "darn",
            "shoot",
            "gosh",
        ],
        "h3ck this fudg!ng thing",
        {
            "@": "a",
            "3": "e",
        },
        [],
    ),
    (
        [
            "dang",
            "darn",
            "heck",
            "gosh",
        ],
        "d@ng it to h3ck",
        {
            "@": "a",
            "3": "e",
        },
        ["d@ng", "h3ck"],
    ),
]
submit_cases = run_cases + [
    (
        [
            "darn",
            "shoot",
            "fudging",
        ],
        "sh00t, I hate this fudg!ng assignment",
        {
            "@": "a",
            "3": "e",
            "0": "o",
            "!": "i",
        },
        ["sh00t", "fudg!ng"],
    ),
]


def test(words, document, variations, expected_matches):
    print("---------------------------------")
    print("Document:")
    print(document)
    print(f"Variations: {variations}")
    print(f"Expected matches: {sorted(expected_matches)}")
    try:
        trie = Trie()
        for word in words:
            trie.add(word)
        actual = sorted(trie.advanced_find_matches(document, variations))
        print(f"Actual matches: {actual}")
        if actual == sorted(expected_matches):
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
