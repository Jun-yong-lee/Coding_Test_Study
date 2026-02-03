import sys
input = sys.stdin.readline

N = int(input())

res = []

for _ in range(N):
    cmd = input().rstrip()
    if len(cmd) != 1:
        cmd, value = map(int, cmd.split())
    else:
        cmd = int(cmd)
    
    if cmd == 1:
        res.append(value)
    elif cmd == 2:
        if len(res) != 0:
            print(res.pop())
        else:
            print("-1")
    elif cmd == 3:
        print(len(res))
    elif cmd == 4:
        if len(res) == 0:
            print("1")
        else:
            print("0")
    elif cmd == 5:
        if len(res) == 0:
            print("-1")
        else:
            print(res[-1])