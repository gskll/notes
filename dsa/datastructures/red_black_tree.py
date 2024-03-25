# A red-black tree is a kind of self-balancing binary search tree. Each node stores an extra bit, which we will call the color, red or black. The color ensures that the tree remains approximately balanced during insertions and deletions.
#
# When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.
#
# In addition to all the properties of a Binary Search Tree, a red-black tree must have the following:
#
#     Each node is either red or black
#     The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
#     All Nil leaf nodes are black.
#     If a node is red, then both its children are black.
#     All paths from a single node go through the same number of black nodes to reach any of its descendant NIL nodes.
#
# The re-balancing of a red-black tree does not result in a perfectly balanced tree. However, its insertion and deletion operations, along with the tree rearrangement and recoloring, are always performed in O(log(n)) time.


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent: RBNode | None = None
        self.val = val
        self.left: RBNode | None = None
        self.right: RBNode | None = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        node = RBNode(val)
        node.left = self.nil
        node.right = self.nil
        node.red = True

        parent = None
        current = self.root

        while current is not self.nil:
            parent = current
            if node.val < current.val and current.left is not None:
                current = current.left
            elif node.val > current.val and current.right is not None:
                current = current.right
            else:
                return  # ignore duplicate

        node.parent = parent
        if parent == None:
            self.root = node
        else:
            if val < parent.val:
                parent.left = node
            if val > parent.val:
                parent.right = node

        self.fix_insert(node)

    def fix_insert(self, node):
        while node is not self.root and node.parent.red:
            if node.parent.right == node:
                if node.parent.parent.right == node.parent:
                    uncle = node.parent.parent.left
                else:
                    uncle = node.parent.parent.right

                if uncle.red:
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node.parent.left == node:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_left(node.parent.parent)
            elif node.parent.left == node:
                if node.parent.parent.right == node.parent:
                    uncle = node.parent.parent.left
                else:
                    uncle = node.parent.parent.right

                if uncle.red:
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node.parent.right == node:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_right(node.parent.parent)

        self.root.red = False

    def rotate_left(self, root):
        if root is self.nil or root.right is self.nil:
            return

        pivot = root.right
        root.right = pivot.left
        if pivot.left is not self.nil:
            pivot.left.parent = root

        pivot.parent = root.parent
        if root.parent is None:
            self.root = pivot
        elif root.parent.right == root:
            root.parent.right = pivot
        elif root.parent.left == root:
            root.parent.left = pivot
        pivot.left = root
        root.parent = pivot

    def rotate_right(self, root):
        if root is self.nil or root.left is self.nil:
            return

        pivot = root.left
        root.left = pivot.right
        if pivot.right is not self.nil:
            pivot.right.parent = root

        pivot.parent = root.parent
        if root.parent is None:
            self.root = pivot
        elif root.parent.right == root:
            root.parent.right = pivot
        elif root.parent.left == root:
            root.parent.left = pivot
        pivot.right = root
        root.parent = pivot


run_cases = [
    (4),
]

submit_cases = run_cases + [
    (10),
]


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


def ref_impl_ins(self, val):
    new_node = RBNode(val)
    new_node.parent = None
    new_node.left = self.nil
    new_node.right = self.nil
    new_node.red = True

    parent = None
    current = self.root
    while current != self.nil:
        parent = current
        if new_node.val < current.val:
            current = current.left
        elif new_node.val > current.val:
            current = current.right
        else:
            # duplicate, just ignore
            return

    new_node.parent = parent
    if parent is None:
        self.root = new_node
    elif new_node.val < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node

    self.ref_impl_fix(new_node)


def ref_impl_fix(self, new_node):
    while new_node != self.root and new_node.parent.red:
        if new_node.parent == new_node.parent.parent.right:
            u = new_node.parent.parent.left
            if u.red:
                u.red = False
                new_node.parent.red = False
                new_node.parent.parent.red = True
                new_node = new_node.parent.parent
            else:
                if new_node == new_node.parent.left:
                    new_node = new_node.parent
                    self.rotate_right(new_node)
                new_node.parent.red = False
                new_node.parent.parent.red = True
                self.rotate_left(new_node.parent.parent)
        else:
            u = new_node.parent.parent.right

            if u.red:
                u.red = False
                new_node.parent.red = False
                new_node.parent.parent.red = True
                new_node = new_node.parent.parent
            else:
                if new_node == new_node.parent.right:
                    new_node = new_node.parent
                    self.rotate_left(new_node)
                new_node.parent.red = False
                new_node.parent.parent.red = True
                self.rotate_right(new_node.parent.parent)
    self.root.red = False


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    return "\n".join(lines)


def format_tree_string(node, lines, level=0):
    if node.val is not None:
        format_tree_string(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        format_tree_string(node.left, lines, level + 1)


setattr(RBTree, "__repr__", print_tree)
setattr(RBTree, "ref_impl_insert", ref_impl_ins)
setattr(RBTree, "ref_impl_fix", ref_impl_fix)


def get_characters(num):
    characters = []
    for i in range(num):
        character = Character(i)
        characters.append(character)
    return characters


def char_list_to_string(char_list):
    character_names = []
    for char in char_list:
        character_names.append(char.character_name)
    return character_names


def test(num_characters):
    characters = get_characters(num_characters)
    tree = RBTree()
    reference_tree = RBTree()
    for character in characters:
        tree.insert(character)
        reference_tree.ref_impl_insert(character)
    print("=====================================")
    print("Expecting:")
    print("-------------------------------------")
    print(reference_tree)
    print("-------------------------------------\n")
    print("Actual:")
    print("-------------------------------------")
    print(tree)
    print("-------------------------------------\n")

    if print_tree(tree) == print_tree(reference_tree):
        print("Pass \n")
        return True
    print("Fail \n")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(test_case)
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
