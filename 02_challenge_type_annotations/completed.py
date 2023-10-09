from typing import Callable, Iterable, Optional, TypeVar


def filter_odd_numbers(numbers:Iterable[int]) -> list[int]:
    """Filters odd numbers from a sequence of numbers."""
    result:list[int] = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result


def square_numbers(numbers:Iterable[float]) -> list[float]:
    """Square numbers in a sequence."""
    result:list[float] = []
    for num in numbers:
        result.append(num**2)
    return result


def count_chars(words:Iterable[str])-> list[int]:
    """Counts the number of characters in a sequence of words."""
    result:list[int] = []
    for word in words:
        result.append(len(word))
    return result


T = TypeVar('T')
def process_data(
    data:T,
    filter_func:Optional[Callable[[T],T]] = None,
    process_func:Optional[Callable[[T],T]] = None,
) -> T:
    """Applies filter_func and process_func on a data sequence."""
    if filter_func is None:
        filter_func = lambda x: x
    filtered_data = filter_func(data)
    if process_func is None:
        process_func = lambda x: x
    return process_func(filtered_data)

#! Correction
# T = TypeVar("T")
# U = TypeVar("U")
#* The function type is declared outside (better if used multiple time)
# FilterFunc = Callable[[T], T]
# ProcessFunc = Callable[[T], U]   #! Process function may not return the same type as the input !


# def process_data(
#     data: T,
#     # ! Looks like we pass the generic type to the custom type so it's consistent inside the function signature
#     filter_func: FilterFunc[T] | None = None,    # ? Is it another way to define Optional as "XXX | None"
#     process_func: ProcessFunc[T, U] | None = None,
# ) -> T | U:
#     """Applies filter_func and process_func on a data sequence."""
#     if filter_func:
#         data = filter_func(data)
#     if process_func:
#         return process_func(data)
#     return data

# ? The filter function seems to imply that the generic T is at least iterable else it would be just a predicate


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = process_data(numbers, filter_odd_numbers, square_numbers)
    print(result)

    words = ["apple", "banana", "cherry"]
    result2 = process_data(words, process_func=count_chars)
    print(result2)


if __name__ == "__main__":
    main()
