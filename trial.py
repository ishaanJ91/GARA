# sample_utils.py

from typing import List

def fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_prime(num: int) -> bool:
    """
    Check if a number is a prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_string(s: str) -> str:
    """
    Return the reversed version of the input string.
    """
    return s[::-1]