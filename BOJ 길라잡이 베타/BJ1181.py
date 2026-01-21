"""
1. 아이디어
- 단어들을 입력받아 종복 제거 후 리스트에 저장
- 길이가 짧은 것부터 정렬
- 길이가 같으면 사전 순으로 정렬

2. 시간복잡도
- 입력: O(N)
- 정렬: O(NlogN)
- 출력: O(N)

3. 변수
- N: int, 단어의 개수
- string_list: list[str], 단어들

"""

import sys

input = sys.stdin.readline
N = int(input())

string_list = list(set([input().rstrip() for _ in range(N)]))
string_list.sort(key=lambda x: (len(x), x)) # sorted_arr = sorted(arr, key=lambda x: 기준)

for each_string in string_list:
    print(each_string)