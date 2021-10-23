def palindromeIndex(s):
    def is_palindrome(s):
        for i in range(len(s) + 1 // 2):
            if s[i] != s[ -1 - i]:
                return False
        return True

    print(s)
    for i in range((len(s) + 1) // 2):
        print(i)
        if s[i] != s[ -1 - i]:
            if is_palindrome(s[i + 1: len(s) - i]):
                return i
            if is_palindrome(s[i:len(s) - i - 1]):
                return len(s) - i - 1
            return -1
    return -1
