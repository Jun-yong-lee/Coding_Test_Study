import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    
    res = []
    for i in range(1, n):
        if n % i == 0:
            res.append(i)
    if sum(res) == n:
        print(f"{n} = " + " + ".join(list(map(str, res))))
    else:
        print(f"{n} is NOT perfect.")