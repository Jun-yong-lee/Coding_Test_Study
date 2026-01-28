import sys
input = sys.stdin.readline

# 조합, 시그마 합

n = int(input())
print(n*(n-1)*(n-2)//6)
print("3")