# Let's solve a commonly misunderstood problem in computer science - finding the prime factors of a number. Almost all modern cryptography, including your browser's HTTPS encryption, is based on the fact that prime factorization is slow. You'll learn why that is later in our Cryptography course.
#
# For now, let's focus on the speed of factorization, and how it relates to the P and NP classes.
#
# Finding a number's prime factors is an algorithm in the NP class.
#
#     When given two primes and their product, all we need to do is a simple multiplication step to verify correctness. (polynomial time)
#     Given just a number, finding its prime factors is a much more difficult problem. (exponential time is the best we know of)
#
# The trouble is that no one has formally proven that there is not a polynomial time algorithm for finding prime factors. So, we're technically unsure if the problem is in P or if it's NP-complete.

# Big O Analysis
#
# Let us denote n as the integer input, and s as the size of n in bits. s = log2(n)
#
# Notice that our first loop iterates log(n) times and the second loop iterates sqrt(n) times. The Big O with respect to n is O(sqrt(n))! That's fast! That's polynomial complexity which would lead us to believe the problem is in P
# Wait!
#
# The problem is that, by definition, when computer scientists talk about this problem, they are talking about the length of n in bits. What we will call s. For example, the integer 255 only takes 8 bits.
#
# 241 = 11110001 in binary
#
# Since s = log2(n), a complexity of O(sqrt(n)) is equivalent to O(sqrt(2^s))
#
# The complexity in respect to the number of bits is exponential.

import math


def prime_factors(n: int) -> list[int]:
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)

    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            factors.append(i)

    if n > 2:
        factors.append(n)

    return factors


run_cases = [(8, [2, 2, 2]), (10, [2, 5]), (24, [2, 2, 2, 3])]

submit_cases = run_cases + [
    (49, [7, 7]),
    (77, [7, 11]),
    (4, [2, 2]),
    (64, [2, 2, 2, 2, 2, 2]),
    (63, [3, 3, 7]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = prime_factors(input1)
    print(f"Actual: {result}")
    if result == expected_output:
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
