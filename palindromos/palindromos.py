import unittest

def palindromos(word):
    word = word.replace(' ', '').lower()
    if len(word) <= 1:
        return True
    if word[0] == word [-1]:
        return palindromos(word[1:-1])
    else:
        return False 
