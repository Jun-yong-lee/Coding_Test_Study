import sys
input = sys.stdin.readline

def factorical(n):
    if n <= 1:
        return 1
    return n * factorical(n-1)

N = int(input())
print(factorical(N))