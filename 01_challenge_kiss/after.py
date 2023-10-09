# version 1
# Creates the dictionnary of unique fruits then iterates thru the list of fruits
# may be a bit too complex and could be writen in one single dictionnary expression


def count_fruits(fruits: list[str]) -> dict[str, int]:
    """Count the number of identical fruits in the list"""
    keys = set(fruits)
    counts = [0] * len(keys)
    d = dict(zip(keys, counts))
    for fruit in fruits:
        d[fruit] += 1
    return d

# TDD approach with unit tests
def count_fruits(fruits: list[str]) -> dict[str,int]:
    return {}

def count_fruits(fruits: list[str]) -> dict[str,int]:
    if not fruits: return {}
    return {fruits[0]:1}

def count_fruits(fruits: list[str]) -> dict[str,int]:
    if not fruits: return {}
    return {fruits[0]:len(fruits)}   

def count_fruits(fruits: list[str]) -> dict[str,int]:
    if not fruits: return {}
    d = dict()
    for fruit in fruits:
        if fruit not in d.keys():
            d[fruit] = 1
        else:
            d[fruit] += 1
    return d



# refactor
def count_fruits(fruits: list[str]) -> dict[str,int]:

    d = dict()
    for fruit in fruits:
        if fruit not in d.keys():
            d[fruit] = 1
        else:
            d[fruit] += 1
    return d

# using Python library
from collections import Counter

def count_fruits(fruits: list[str]) -> dict[str,int]:
    return dict(Counter(fruits))

def main() -> None:

    # degenerated case
    assert count_fruits([]) == {}
    
    assert count_fruits(["apple"]) == {"apple":1}

    assert count_fruits(["apple", "apple"]) == {"apple":2}

    assert count_fruits(["apple", "apple", "banana"]) == {"apple":2, "banana":1}

    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}

    from random import choices
    # Genereate a super long list of fruits for performance comparison
    unique_fruits = ["apple", "banana", "cherry"]
    fruits = choices(unique_fruits,k=10_000_000)

    import time

    t = time.process_time()
    count_fruits(fruits)
    elapsed_time = time.process_time() - t
    print(elapsed_time)

if __name__ == "__main__":
    main()
