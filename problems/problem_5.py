def longest_palindrome(s: str) -> str:
    l_palindrome = s[0]
    s_length = len(s)

    for i, char in enumerate(s):
        next_char = s[i + 1] if i + 1 < s_length else None

        for add_next_index in range(2 if next_char == char else 1):
            palindrome = char if add_next_index == 0 else char + char

            for j in range(1, 1 + min(i + 1, s_length - i)):
                prev_char = s[i - j] if i - j >= 0 else None
                next_char = s[i + j + add_next_index] if i + j + add_next_index < s_length else None

                if prev_char != next_char or prev_char is None:
                    break

                palindrome = prev_char + palindrome + next_char

            if len(palindrome) > len(l_palindrome):
                l_palindrome = palindrome

    return l_palindrome


result = longest_palindrome("aaa")
print(result)
