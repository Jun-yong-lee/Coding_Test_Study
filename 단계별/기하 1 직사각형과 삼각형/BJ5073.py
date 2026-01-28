import sys
input = sys.stdin.readline

while True:
    abc = list(map(int, input().split()))
    if abc[0] == 0 and abc[1] == 0 and abc[2] == 0:
        break
    if max(abc) >= (sum(abc) - max(abc)):
        print("Invalid")
    elif abc[0] == abc[1] == abc[2]:
        print("Equilateral")
    elif abc[0] == abc[1] or abc[1] == abc[2] or abc[0] == abc[2]:
        print("Isosceles")
    else:
        print("Scalene")