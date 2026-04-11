def solution(answers):
    answer = []
    supoza1 = [1, 2, 3, 4, 5]
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    
    for i in range(len(answers)):
        if supoza1[i%5] == answers[i]:
            cnt[0] += 1
        if supoza2[i%8] == answers[i]:
            cnt[1] += 1
        if supoza3[i%10] == answers[i]:
            cnt[2] += 1
    v_max = max(cnt)
    for j in range(3):
        if v_max == cnt[j]:
            answer.append(j+1)
    
    return answer