from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    current_weight = 0
    
    while bridge:
        exit_truck_weight = bridge.popleft()
        current_weight -= exit_truck_weight
        
        if trucks:
            if current_weight + trucks[0] <= weight:
                now_truck = trucks.popleft()
                bridge.append(now_truck)
                current_weight += now_truck
            else:
                bridge.append(0)
        answer += 1
    
    return answer