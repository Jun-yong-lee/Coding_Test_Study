import sys
input = sys.stdin.readline

X = int(input())

k = 1

# k번째 대각선의 끝 번호
while X > k * (k + 1) // 2:
    k += 1

prev_sum = (k - 1) * k // 2
index = X - prev_sum # k번째 대각선에서 몇 번째인지

if k % 2 == 1: # 홀수 대각선: 분자 크게 시작
    numerator = k - index + 1
    denominator = index
else:
    numerator = index
    denominator = k - index + 1

print(str(numerator)+"/"+str(denominator))