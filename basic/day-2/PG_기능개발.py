from collections import deque

def solution(progresses, speeds):
    answer = []
    
    queue_p = deque(progresses)
    queue_s = deque(speeds)
    
    while queue_p:
        count = 0
        for i in range(len(queue_p)):
            queue_p[i] += queue_s[i]
            
        while queue_p and queue_p[0] >= 100:
            queue_p.popleft()
            queue_s.popleft()
            count += 1
        if count != 0:
            answer.append(count)
    return answer