from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 1. 2배 확장된 맵 초기화
    field = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = r[0] * 2, r[1] * 2, r[2] * 2, r[3] * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0 # 내부 0
                elif field[i][j] != 0:
                    field[i][j] = 1 # 테두리 1
                    
    # 2. BFS
    q = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, dist = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            return dist // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 102 and 0 <= ny < 102 and field[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))