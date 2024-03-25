import random

# Instead of a list of children, each node has at most 2 children, a right and a left child
# The left child's value must be less than its parent's value
# The right child's value must be greater than its parents
# No two nodes in the BST can have the same value
#
# BST's have a problem. While it's true that on average a BST has O(log(n)) lookups, deletions, and insertions, that fundamental benefit can break down quickly.
# If mostly sorted data, or even worse, completely sorted data, is inserted into a binary tree, the tree will be much deeper than it is wide. As you know by now, the complexity of the tree's operations depend entirely on the depth of the tree.
# A balanced tree will always have the minimum height possible for the number of elements it contains.


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if self.val > val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
            return

        if self.val < val:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
            return

    def get_max(self):
        if self.right is None:
            return self.val

        curr = self.right
        while curr and curr.right:
            curr = curr.right
        return curr.val

    def get_min(self):
        if self.left is None:
            return self.val

        curr = self.left
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def delete(self, val):
        if self.val is None:
            return None

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_larger_node = self.right.get_min()
        self.val = min_larger_node
        self.right = self.right.delete(min_larger_node)
        return self

    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited

    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited

    def exists(self, val):
        if self.val == val:
            return True

        if self.left and self.left.exists(val):
            return True

        if self.right and self.right.exists(val):
            return True

        return False

    def height(self):
        if self.val is None:
            return 0

        left_height, right_height = 0, 0
        if self.left:
            left_height = self.left.height()
        if self.right:
            right_height = self.right.height()

        return max(left_height, right_height) + 1


run_cases = [(1, 1), (3, 3), (10, 7)]

submit_cases = run_cases + [(20, 7)]


class Character:
    def __init__(self, gamertag):
        self.gamertag = gamertag
        character_names = [
            "Ebork",
            "Astram",
            "Elian",
            "Tarlock",
            "Grog",
            "Myra",
            "Sullivan",
            "Marlo",
            "Jax",
            "Anthony",
            "Bhurdan",
            "Thoreuth",
            "Bob",
            "Varis",
            "Nyx",
            "Luna",
            "Ash",
            "Rhogar",
            "Ember",
            "Mikel",
            "Yamil",
            "Velithria",
        ]
        self.character_name = (
            f"{character_names[gamertag%len(character_names)]}#{gamertag}"
        )

    def __eq__(self, other):
        return self.gamertag == other.gamertag

    def __lt__(self, other):
        return self.gamertag < other.gamertag

    def __gt__(self, other):
        return self.gamertag > other.gamertag

    def __repr__(self):
        return "".join(self.character_name)


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    return "\n".join(lines)


def format_tree_string(bst_node, lines, level=0):
    if bst_node != None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


setattr(BSTNode, "__repr__", print_tree)


def get_characters(num):
    random.seed(1)
    characters = []
    gamertags = []
    for i in range(num * 3):
        gamertags.append(i)
    random.shuffle(gamertags)
    gamertags = gamertags[:num]
    for gamertag in gamertags:
        character = Character(gamertag)
        characters.append(character)
    return characters


def char_list_to_string(char_list):
    character_names = []
    for char in char_list:
        character_names.append(char.character_name)
    return character_names


def test(num_characters, expected):
    characters = get_characters(num_characters)
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print(bst)
    print("-------------------------------------\n")
    print(f"Expecting Height: {expected}")
    try:
        actual = bst.height()
        print(f"Actual Height: {actual}")
        if expected == actual:
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
