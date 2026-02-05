import sys
input = sys.stdin.readline

def recursion(s, l, r, c):
    if l >= r:
        return 1, c
    elif s[l] != s[r]:
        return 0, c
    else:
        c += 1
        return recursion(s, l+1, r-1, c)

def isPalindrome(s):
    c = 1
    is_recursion, c = recursion(s, 0, len(s)-1, c)
    return is_recursion, c

T = int(input())

for _ in range(T):
    s = input().rstrip()
    is_recursion, count = isPalindrome(s)
    print(is_recursion, count)