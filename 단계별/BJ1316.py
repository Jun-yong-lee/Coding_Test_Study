import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
count = 0

for each_word in words:
    segments = {}
    segments[each_word[0]] = 1

    for i in range(1, len(each_word)):
        if each_word[i] != each_word[i-1]:
            segments[each_word[i]] = segments.get(each_word[i], 0) + 1
    if max(segments.values()) == 1:
        count += 1
print(count)