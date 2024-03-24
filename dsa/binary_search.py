import time


def binary_search(data: list[dict], followers: int) -> str | None:
    def search(low: int, high: int) -> str | None:
        if low > high:
            return None

        mid = low + (high - low) // 2

        if data[mid]["followers"] == followers:
            return data[mid]["name"]
        elif data[mid]["followers"] < followers:
            return search(mid + 1, high)
        else:
            return search(low, mid - 1)

    return search(0, len(data) - 1)


run_cases = [
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 10},
            {"name": "James", "followers": 15},
            {"name": "Judy", "followers": 20},
        ],
        10,
        "Jane",
    ),
    (
        [
            {"name": "Bob", "followers": 25},
            {"name": "Boris", "followers": 30},
            {"name": "Borice", "followers": 35},
        ],
        30,
        "Boris",
    ),
]

submit_cases = run_cases + [
    ([], 10, None),
    ([{"name": "John", "followers": 5}], 5, "John"),
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 10},
            {"name": "James", "followers": 15},
            {"name": "Judy", "followers": 20},
        ],
        22,
        None,
    ),
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 10},
            {"name": "James", "followers": 15},
            {"name": "Judy", "followers": 20},
        ],
        5,
        "John",
    ),
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 20},
            {"name": "James", "followers": 25},
            {"name": "Borice", "followers": 50},
            {"name": "Boris", "followers": 55},
            {"name": "Donald", "followers": 60},
            {"name": "Doris", "followers": 65},
            {"name": "Derek", "followers": 70},
            {"name": "Diana", "followers": 75},
            {"name": "Dennis", "followers": 80},
            {"name": "Daisy", "followers": 85},
            {"name": "Duke", "followers": 90},
            {"name": "George", "followers": 95},
            {"name": "Fred", "followers": 100},
            {"name": "Elena", "followers": 105},
            {"name": "Evan", "followers": 110},
            {"name": "Emma", "followers": 115},
            {"name": "Ethan", "followers": 120},
            {"name": "Ellie", "followers": 125},
            {"name": "Eddie", "followers": 130},
            {"name": "Elise", "followers": 135},
            {"name": "Ezra", "followers": 140},
            {"name": "Esther", "followers": 145},
            {"name": "Elijah", "followers": 150},
            {"name": "Erin", "followers": 155},
            {"name": "Eric", "followers": 160},
            {"name": "Elaine", "followers": 165},
            {"name": "Eugene", "followers": 170},
            {"name": "Winston", "followers": 175},
            {"name": "Waylen", "followers": 180},
        ],
        180,
        "Waylen",
    ),
    (
        [
            {"name": "Xi", "followers": 0},
            {"name": "Alice", "followers": 1},
            {"name": "Bob", "followers": 2},
            {"name": "Charlie", "followers": 3},
            {"name": "Diana", "followers": 4},
            {"name": "Evan", "followers": 5},
            {"name": "Fiona", "followers": 6},
            {"name": "George", "followers": 7},
            {"name": "Hannah", "followers": 8},
            {"name": "Ian", "followers": 9},
            {"name": "Julia", "followers": 10},
            {"name": "Kevin", "followers": 11},
            {"name": "Linda", "followers": 12},
            {"name": "Mike", "followers": 13},
            {"name": "Nina", "followers": 14},
            {"name": "Oscar", "followers": 15},
            {"name": "Pam", "followers": 16},
            {"name": "Quincy", "followers": 17},
            {"name": "Rachel", "followers": 18},
            {"name": "Steve", "followers": 19},
            {"name": "Tina", "followers": 20},
            {"name": "Umar", "followers": 21},
            {"name": "Vivian", "followers": 22},
            {"name": "Walter", "followers": 23},
            {"name": "Xena", "followers": 24},
            {"name": "Yves", "followers": 25},
            {"name": "Zara", "followers": 26},
            {"name": "Adam", "followers": 27},
            {"name": "Betty", "followers": 28},
            {"name": "Carlos", "followers": 29},
            {"name": "Debbie", "followers": 30},
            {"name": "Edward", "followers": 31},
            {"name": "Flora", "followers": 32},
            {"name": "Gary", "followers": 33},
            {"name": "Heidi", "followers": 34},
            {"name": "Igor", "followers": 35},
            {"name": "Jenny", "followers": 36},
            {"name": "Kyle", "followers": 37},
            {"name": "Laura", "followers": 38},
            {"name": "Mason", "followers": 39},
            {"name": "Nora", "followers": 40},
            {"name": "Oliver", "followers": 41},
            {"name": "Paula", "followers": 42},
            {"name": "Quentin", "followers": 43},
            {"name": "Rose", "followers": 44},
            {"name": "Sam", "followers": 45},
            {"name": "Tracy", "followers": 46},
            {"name": "Uriel", "followers": 47},
            {"name": "Vanessa", "followers": 48},
            {"name": "Will", "followers": 49},
            {"name": "Xander", "followers": 50},
            {"name": "Yolanda", "followers": 51},
            {"name": "Zack", "followers": 52},
            {"name": "Amelia", "followers": 53},
            {"name": "Ben", "followers": 54},
            {"name": "Cynthia", "followers": 55},
            {"name": "Derek", "followers": 56},
            {"name": "Elsa", "followers": 57},
            {"name": "Fred", "followers": 58},
            {"name": "Gloria", "followers": 59},
            {"name": "Henry", "followers": 60},
            {"name": "Isabel", "followers": 61},
            {"name": "Jack", "followers": 62},
            {"name": "Karen", "followers": 63},
            {"name": "Leo", "followers": 64},
            {"name": "Maggie", "followers": 65},
            {"name": "Neil", "followers": 66},
            {"name": "Olivia", "followers": 67},
            {"name": "Pete", "followers": 68},
            {"name": "Queen", "followers": 69},
            {"name": "Ralph", "followers": 70},
            {"name": "Sandy", "followers": 71},
            {"name": "Tabitha", "followers": 72},
            {"name": "Ulysses", "followers": 73},
            {"name": "Valerie", "followers": 74},
            {"name": "Wesley", "followers": 75},
            {"name": "Xiomara", "followers": 76},
            {"name": "Yanni", "followers": 77},
            {"name": "Zelda", "followers": 78},
            {"name": "Ariana", "followers": 79},
            {"name": "Braxton", "followers": 80},
            {"name": "Cecilia", "followers": 81},
            {"name": "Dominic", "followers": 82},
            {"name": "Emery", "followers": 83},
            {"name": "Felicity", "followers": 84},
            {"name": "Gideon", "followers": 85},
            {"name": "Harper", "followers": 86},
            {"name": "Isaiah", "followers": 87},
            {"name": "Jolene", "followers": 88},
            {"name": "Kai", "followers": 89},
            {"name": "Lorelei", "followers": 90},
            {"name": "Mitchell", "followers": 91},
            {"name": "Nadine", "followers": 92},
            {"name": "Orlando", "followers": 93},
            {"name": "Phoebe", "followers": 94},
            {"name": "Quinton", "followers": 95},
            {"name": "Rosalind", "followers": 96},
            {"name": "Shane", "followers": 97},
            {"name": "Talia", "followers": 98},
            {"name": "Uriah", "followers": 99},
            {"name": "Vince", "followers": 100},
            {"name": "Willa", "followers": 101},
            {"name": "Xavier", "followers": 102},
            {"name": "Yasmin", "followers": 103},
            {"name": "Zane", "followers": 104},
            {"name": "Audrey", "followers": 105},
            {"name": "Bryce", "followers": 106},
            {"name": "Carla", "followers": 107},
            {"name": "Dalton", "followers": 108},
            {"name": "Elaine", "followers": 109},
            {"name": "Fernando", "followers": 110},
            {"name": "Geneva", "followers": 111},
            {"name": "Hugo", "followers": 112},
            {"name": "Irene", "followers": 113},
            {"name": "Jerome", "followers": 114},
            {"name": "Kelsey", "followers": 115},
            {"name": "Leon", "followers": 116},
            {"name": "Mona", "followers": 117},
            {"name": "Nolan", "followers": 118},
            {"name": "Octavia", "followers": 119},
            {"name": "Preston", "followers": 120},
            {"name": "Quinn", "followers": 121},
            {"name": "Rita", "followers": 122},
            {"name": "Sylvester", "followers": 123},
            {"name": "Trina", "followers": 124},
            {"name": "Ulric", "followers": 125},
            {"name": "Vera", "followers": 126},
            {"name": "Winston", "followers": 127},
            {"name": "Xena", "followers": 128},
            {"name": "York", "followers": 129},
            {"name": "Zoey", "followers": 130},
            {"name": "Ashton", "followers": 131},
            {"name": "Brittany", "followers": 132},
            {"name": "Carter", "followers": 133},
            {"name": "Deanna", "followers": 134},
            {"name": "Elliot", "followers": 135},
            {"name": "Francesca", "followers": 136},
            {"name": "Grant", "followers": 137},
            {"name": "Hazel", "followers": 138},
            {"name": "Ian", "followers": 139},
            {"name": "Joanna", "followers": 140},
            {"name": "Kurt", "followers": 141},
        ],
        141,
        "Kurt",
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs")
    print(f" * Data: {input1}")
    print(f" * Follower count to search: {input2}")
    print(f"Expected: {expected_output} & completed in less than 5 microseconds")
    start = time.time()
    result = binary_search(input1, input2)
    end = time.time()
    timeout = 0.000005
    print(f"binary_search completed in {(end - start) * 1_000_000} microseconds")
    in_time = end - start < timeout
    if not in_time:
        print(f"binary_search took too long, speed it up!")
    print(f"Actual: {result}")
    if result == expected_output and in_time:
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
