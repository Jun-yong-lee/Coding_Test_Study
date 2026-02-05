import sys
input = sys.stdin.readline

N, M = map(int, input().split())
word_dict = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    else:
        word_dict[word] = word_dict.get(word, 0) + 1
res = []
for k, v in word_dict.items():
    res.append([k, v, len(k)]) # "append"->사전순 활용, 중복 수, 길이

res = sorted(res, key=lambda x:(-x[1], -x[2], x[0]))
# 1. 자주 나오는 단어일수록 앞에 배치 -> 내림차순
# 2. 해당 단어의 길이가 길수록 앞에 배치 -> 내림차순
# 3. 앞파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치 -> 오름차순
for i in res:
    print(i[0])