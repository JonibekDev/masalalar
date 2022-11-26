def is_palindrome(word):

    low = 0
    high = len(word) - 1

    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1
    return True

word = 'aziza'

print(is_palindrome(word))