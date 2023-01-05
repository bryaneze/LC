# Simple solution
def isPalindrome(s):
    newStr = ""
    # remove non alphanumeric
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


# 2 pointer solution
def isPalindrome(s):
    def alphaNum(c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    left = 0
    right = len(s) - 1

    while left < right:

        while left < right and not alphaNum(
            s[left]
        ):  # left < right condition, to make sure left pointer doesn't go past right
            left += 1
        while right > left and not alphaNum(
            s[right]
        ):  # right > left condition, to make sure right pointer doesn't go past left
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
