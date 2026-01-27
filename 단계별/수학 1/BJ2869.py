# 시간복잡도를 고려해서 코딩할 필요 존재

import sys
input = sys.stdin.readline
import math

A, B, V = map(int, input().split())
days = math.ceil((V - A) / (A - B)) + 1
print(days)