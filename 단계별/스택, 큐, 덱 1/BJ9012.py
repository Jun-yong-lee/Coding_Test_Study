import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    res = []
    possible = True

    strings_list = list(input().rstrip())
    for each_string in strings_list:
        if each_string == "(":
            res.append("(")
        else:
            if len(res) == 0:
                possible = False
                break
            res.pop()
    if len(res) == 0 and possible == True:
        print("YES")
    else:
        print("NO")

# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(