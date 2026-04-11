from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    combi_list = []
    arr = []

    for i in range(1, len(num_list)+1):
        combi = permutations(num_list, i)
        for j in combi:
            combi_list.append(j)
    
    for j in range(len(combi_list)):
        arr.append(int("".join(combi_list[j])))
    arr = list(set(arr))
    
    for k in range(len(arr)):
        if is_prime(arr[k]):
            answer += 1
    return answer