import sys
input = sys.stdin.readline

N = int(input())
res = [0] * 16
res[1] = 9
for i in range(2, N+1):
    res[i] = int((res[i-1]**(0.5) * 2 - 1)**2)
    
print(res[N])