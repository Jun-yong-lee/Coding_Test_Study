import heapq

def solution(N, road, K):
    answer = 0

    graph = [[] for i in range(N+1)]
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    dist = [float("inf")] * (N+1)
    dist[1] = 0
    
    queue = [(0, 1)]
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if dist[current_node] < current_dist:
            continue

        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight

            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(queue, (new_dist, next_node))
    count = 0
    for i in dist:
        if i <= K:
            count += 1
    return count