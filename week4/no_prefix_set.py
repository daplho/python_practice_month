import math
import os
import random
import re
import sys

class SimpleTrie:
    def __init__(self):
        self.trie = {}
    
    # if prefix is found return True
    # otherwise add the string to the trie
    def check_prefix(self, s):
        # pointer to the current node (walker)
        w = self.trie
        for i,c in enumerate(s):
            # if current character is not in current node
            # add it as either end of word or empty dictionary
            if c not in w:
                w[c] = 'eow' if i == len(s) - 1 else {}
            # else return true if it's end of word or the last character.
            # if it's end of word than an existing word is a prefix
            # of the current word. If it's the end of the current word
            # than the current word is a prefix of existing word
            elif w[c] == 'eow' or i == len(s) - 1:
                return True
            # set walker to current node        
            w = w[c]
        
        return False
#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    trie = SimpleTrie()
    for word in words:
        if trie.check_prefix(word):
            print("BAD SET")
            print(word)
            return
    
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)