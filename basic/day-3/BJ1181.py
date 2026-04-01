import sys

input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())
words = list(set(words))
words.sort(key=lambda x:[len(x), x])

for each_word in words:
    print(each_word)

# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours