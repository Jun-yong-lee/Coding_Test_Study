# 큐 사용
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        now_price = queue.popleft()
        count = 0
        for i in queue:
            count += 1
            if now_price > i:
                break
        answer.append(count)
    
    return answer


# 스택 사용
def solution(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        answer[i] = n - 1 - i
    waiting_room = []
    
    for current_time in range(n):
        while waiting_room and prices[current_time] < prices[waiting_room[-1]]:
            past_time = waiting_room.pop()
            answer[past_time] = current_time - past_time
            
        waiting_room.append(current_time)
        
    return answer