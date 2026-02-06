import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0           # 저장 횟수 카운트
answer = -1       # K번째 저장 값 (못 찾으면 -1 유지)
tmp = [0] * N     # 한 번만 만들어 재사용

def merge(A, p, q, r):
    global cnt, answer

    i = p
    j = q + 1
    t = p  # tmp에서 쓸 인덱스를 A와 같은 구간으로 맞춤

    # 두 구간 병합
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    # 왼쪽 부분 남은 경우
    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1

    # 오른쪽 부분 남은 경우
    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1

    # tmp를 다시 A[p..r]로 복사
    for idx in range(p, r + 1):
        A[idx] = tmp[idx]
        cnt += 1
        if cnt == K:
            answer = A[idx]


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


merge_sort(A, 0, N - 1)
print(answer)
