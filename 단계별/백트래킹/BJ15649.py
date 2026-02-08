import sys

input = sys.stdin.readline

N, M = map(int, input().split())

seq = []

def backtracking():
    if len(seq) == M:
        print(" ".join(list(map(str, seq))))
        return
    
    for i in range(1, N+1):
        if i not in seq:
            seq.append(i)
            backtracking()
            seq.pop()

backtracking()

# 4 2