from collections import deque

def solution(maps):
    answer = 0
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] == 1:
                        maps[nx][ny] = maps[x][y] + 1
                        queue.append((nx, ny))

    bfs(0, 0)
    answer = maps[-1][-1]
    if answer == 1:
        answer = -1
    return answer