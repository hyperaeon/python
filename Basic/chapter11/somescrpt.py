__author__ = 'hzliyong'

import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print("wordCount: " + wordcount)