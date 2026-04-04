from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    start_pos = None
    for r in range(n):
        for c in range(m):
            if board[r][c] == "R":
                start_pos = (r, c)
                
    queue = deque([(start_pos[0], start_pos[1], 0)]) # x, y, count
    visited = [[False] * m for _ in range(n)]
    visited[start_pos[0]][start_pos[1]] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, dist = queue.popleft()
        if board[x][y] == "G":
            return dist
        
        for i in range(4):
            nx = x
            ny = y
            
            while True:
                next_x = nx + dx[i]
                next_y = ny + dy[i]
                
                # 지도 안이고 장애물이 아니라면 계속 전진
                if 0 <= next_x < n and 0 <= next_y < m and board[next_x][next_y] != "D":
                    nx = next_x
                    ny = next_y
                else:
                    break
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, dist + 1])
    return -1