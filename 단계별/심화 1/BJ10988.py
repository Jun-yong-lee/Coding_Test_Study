import sys
input = sys.stdin.readline

words = input().rstrip()
l_words = len(words)

if l_words % 2 ==0:
    if words[l_words//2:] == words[:l_words//2][::-1]: print("1")
    else: print("0")
else:
    if words[(l_words//2+1):] == words[:(l_words//2)][::-1]: print("1")
    else: print("0")