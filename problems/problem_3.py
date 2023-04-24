import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def length_of_longest_substring(s: str) -> int:
    s_length = len(s)
    longest_substring_length = 0 if s_length == 0 else 1

    for i in range(s_length - 1):
        substring = s[i]

        for j in range(i + 1, s_length):
            char = s[j]

            if char not in substring:
                substring += char
            else:
                break

        if len(substring) > longest_substring_length:
            longest_substring_length = len(substring)

    return longest_substring_length


result = length_of_longest_substring("au")
print(result)
