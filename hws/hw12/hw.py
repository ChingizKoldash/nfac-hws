from typing import List, Any, Dict, Set, Generator

"""
Exercise-1: List Comprehension to Squares
Write a function "squares(n: int) -> List[int]" that uses a list comprehension to return a list of the squares of all numbers up to 'n'.

Example:
squares(5) -> [0, 1, 4, 9, 16]
"""
def squares(n: int):
    return [i**2 for i in range(0,n)]

"""
Exercise-2: Set Comprehension with Filtering
Write a function "unique_squares(numbers: List[int]) -> Set[int]" that uses a set comprehension to return the squares of the unique numbers from the input list.

Example:
unique_squares([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) -> {1, 4, 9, 16}
"""
def unique_squares(numbers: List[int]) -> Set[int]:
    return {i**2 for i in numbers}

"""
Exercise-3: Dictionary Comprehension to Count Characters
Write a function "char_counts(text: str) -> Dict[str, int]" that uses a dictionary comprehension to count the occurrence of each character in a string.

Example:
char_counts("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""
def char_counts(text: str) -> Dict[str, int]:
    return {char: text.count(char) for char in set(text)}

"""
Exercise-4: Nested List Comprehension
Write a function "flatten(nested_list: List[List[Any]]) -> List[Any]" that uses a nested list comprehension to flatten a list of lists.

Example:
flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
def flatten(nested_list: List[List[Any]]) -> List[Any]:
    return [i for sublist in nested_list for i in sublist]
    

"""
Exercise-5: Generator Expression to Yield Squares
Write a function "squares_gen(n: int) -> Generator[int]" that uses a generator expression to yield the squares of all numbers up to 'n'.

Example:
list(squares_gen(5)) -> [0, 1, 4, 9, 16]
"""
def squares_gen(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i ** 2

"""
Exercise-6: Set Comprehension to Find Odd Squares
Write a function "odd_squares(n: int) -> Set[int]" that uses a set comprehension to find the squares of all odd numbers up to 'n'.

Example:
odd_squares(10) -> {1, 9, 25, 49, 81}
"""
def odd_squares(n: int) -> set[int]:
    return {i**2 for i in range(1, n+1, 2)}

"""
Exercise-7: Dictionary Comprehension to Map Indices
Write a function "index_map(text: str) -> Dict[str, int]" that uses a dictionary comprehension to map each character in a string to its index.

Example:
index_map("hello") -> {'h': 0, 'e': 1, 'l': 3, 'o': 4}
"""
def index_map(text: str) -> dict[str, int]:
    return {item: index for index,item in enumerate(text)}

"""
Exercise-8: Nested Set Comprehension
Write a function "unique_values(nested_list: List[List[Any]]) -> Set[Any]" that uses a nested set comprehension to find the unique values in a nested list.

Example:
unique_values([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> {1, 2, 3, 4, 5}
"""
def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    return {i for sublist in nested_list for i in sublist}

"""
Exercise-9: Fibonacci Sequence with Generators
Write a function "fibonacci_gen(n: int) -> Generator[int]" that uses a generator to yield the Fibonacci sequence up to the nth term.

Example:
list(fibonacci_gen(10)) -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""
def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


"""
Exercise-10: Dictionary Comprehension to Invert a Dictionary
Write a function "invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]" that uses a dictionary comprehension to invert a dictionary.

Example:
invert_dict({'a': 1, 'b': 2, 'c': 3}) -> {1: 'a', 2: 'b', 3: 'c'}
"""
def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return {value : key for key,value in d.items()}

"""
Exercise-11: Prime Numbers with List Comprehension
Write a function "primes(n: int) -> List[int]" that uses a list comprehension to return a list of all prime numbers up to 'n'.

Example:
primes(10) -> [2, 3, 5, 7]
"""
def primes(n: int) -> List[int]:
    return [x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

"""
Exercise-12: Set Comprehension to Intersect Sets
Write a function "intersection(sets: List[Set[Any]]) -> Set[Any]" that uses a set comprehension to return the intersection of a list of sets.

Example:
intersection([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]) -> {3}
"""
def intersection(sets: List[Set[Any]]) -> Set[Any]:
    return {elem for elem in sets[0] if all(elem in s for s in sets[1:])} 

"""
Exercise-13: Generator Expression to Yield Factorials
Write a function "factorials_gen(n: int) -> Generator[int]" that uses a generator expression to yield the factorials of all numbers up to 'n'.

Example:
list(factorials_gen(5)) -> [1, 2, 6, 24, 120]
"""
def factorials_gen(n: int) -> Generator[int, None, None]:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        yield fact

"""
Exercise-14: Dictionary Comprehension to Map Strings to Lengths
Write a function "str_lengths(strings: List[str]) -> Dict[str, int]" that uses a dictionary comprehension to map strings to their lengths.

Example:
str_lengths(['hello', 'world', 'python']) -> {'hello': 5, 'world': 5, 'python': 6}
"""
def str_lengths(strings: List[str]) -> Dict[str, int]:
    return {string: len(string) for string in strings}

"""
Exercise-15: Nested List Comprehension to Transpose Matrix
Write a function "transpose(matrix: List[List[Any]]) -> List[List[Any]]" that uses a nested list comprehension to transpose a matrix.

Example:
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""
def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


"""
Exercise-16: Generator to Yield Reversed List
Write a function "reverse_gen(lst: List[Any]) -> Generator[Any]" that returns a generator which yields elements from the list in reverse order.

Example:
list(reverse_gen([1, 2, 3, 4, 5])) -> [5, 4, 3, 2, 1]
"""
def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    for item in reversed(lst):
        yield item

"""
Exercise-17: Dictionary Comprehension to Group By Length
Write a function "group_by_length(words: List[str]) -> Dict[int, List[str]]" that uses a dictionary comprehension to group words by their length.

Example:
group_by_length(['hello', 'world', 'python', 'is', 'fun']) -> {5: ['hello', 'world'], 6: ['python'], 2: ['is'], 3: ['fun']}
"""
def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    return {length: [word for word in words if len(word) == length] for length in set(map(len, words))}

"""
Exercise-18: Set Comprehension to Find Common Elements
Write a function "common_elements(lists: List[List[Any]]) -> Set[Any]" that uses a set comprehension to find the common elements in a list of lists.

Example:
common_elements([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) -> {3}
"""
def common_elements(lists: List[List[Any]]) -> Set[Any]:
    return {element for element in lists[0] if all(element in lst for lst in lists[1:])}

"""
Exercise-19: Generator Expression to Yield Primes
Write a function "primes_gen(n: int) -> Generator[int]" that uses a generator expression to yield all prime numbers up to 'n'.

Example:
list(primes_gen(10)) -> [2, 3, 5, 7]
"""
def primes_gen(n: int) -> Generator[int, None, None]:
    return (x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))

"""
Exercise-20: Dictionary Comprehension to Convert List to Dict
Write a function "list_to_dict(lst: List[Any]) -> Dict[int, Any]" that uses a dictionary comprehension to convert a list into a dictionary where the keys are the indices of the list elements.

Example:
list_to_dict(['a', 'b', 'c']) -> {0: 'a', 1: 'b', 2: 'c'}
"""
def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    return {i: lst[i] for i in range(len(lst))}