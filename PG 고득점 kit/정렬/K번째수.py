def solution(array, commands):
    answer = []
    for each_command in commands:
        i, j, k = each_command
        n_arr = array[i-1:j]
        n_arr.sort()
        answer.append(n_arr[k-1])
    return answer