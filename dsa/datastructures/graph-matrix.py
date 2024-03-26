class Graph:
    def __init__(self, num_vertices):
        self.graph = [[False for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]


run_cases = [
    (
        3,
        [
            (0, 1),
            (2, 0),
        ],
        (
            [
                (1, 0),
                (1, 2),
                (2, 0),
            ],
            [True, False, True],
        ),
    ),
    (
        6,
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        (
            [
                (0, 1),
                (1, 2),
                (0, 4),
                (2, 5),
                (5, 0),
            ],
            [True, True, False, False, False],
        ),
    ),
]
submit_cases = run_cases + [
    (
        6,
        [
            (0, 1),
            (2, 4),
            (2, 1),
            (3, 1),
            (4, 5),
        ],
        (
            [
                (5, 4),
                (1, 5),
                (0, 4),
                (2, 5),
                (1, 3),
            ],
            [True, False, False, False, True],
        ),
    ),
]


def test(num_of_vertices, edges_to_add, edges_to_check):
    print("=================================")
    graph = Graph(num_of_vertices)
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("---------------------------------")
    try:
        actual = []
        for i, edge in enumerate(edges_to_check[0]):
            exists = graph.edge_exists(edge[0], edge[1])
            actual.append(exists)
            print(f"{edge} exists:")
            print(f" - Expecting: {edges_to_check[1][i]}")
            print(f" - Actual: {exists}")
        if actual == edges_to_check[1]:
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
