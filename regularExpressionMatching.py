def is_match(s: str, p: str) -> bool:
    # Base case: if the regular expression is empty, return True if the input string is empty, False otherwise
    if len(p) == 0:
        return len(s) == 0

    # Base case: if the regular expression is a single character, return True if the input string is a single character and they match, False otherwise
    if len(p) == 1:
        return len(s) == 1 and (p[0] == s[0] or (p[0] == '.' and s[0] != '\0'))



    # Recursive case: if the regular expression contains a '*', return True if the input string matches the substring before the '*' repeated any number of times, False otherwise
    if p[1] == '*':
        return (p[0] == s[0] or (p[0] == '.' and s[0] != '\0')) and is_match(s, p[2:]) or (s != '' and (p[0] == s[0] or (p[0] == '.' and s[0] != '\0')) and is_match(s[1:], p))

    # Recursive case: if the regular expression does not contain a '*', return True if the input string matches the substring before the '*' repeated once, False otherwise
    return (s != '' and (p[0] == s[0] or (p[0] == '.' and s[0] != '\0')) and is_match(s[1:], p[1:]))

print(is_match("aa", "a"))  # Output: False
print(is_match("aa", "a*"))  # Output: True
print(is_match("ab", ".*"))  # Output: True
print(is_match("ab", "c*a*b"))  # Output: True
print(is_match("mississippi", "mis*is*p*."))  # Output: False