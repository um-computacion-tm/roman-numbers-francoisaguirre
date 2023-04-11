import unittest

def palindrome(word):
    word = word.replace(' ', '').lower()
    if len(word) <= 1:
        return True
    if word[0] == word [-1]:
        return palindrome(word[1:-1])
    else:
        return False 
